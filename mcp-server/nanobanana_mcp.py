#!/usr/bin/env python3
"""
Nanobanana MCP Server for Claude Desktop

This MCP server provides tools for generating and editing images using
the Nanobanana Pro (Gemini 3 Pro Image) API.

Installation:
    pip install mcp google-genai

Usage:
    Set GOOGLE_API_KEY environment variable
    Run: python nanobanana_mcp.py

Claude Desktop Configuration (claude_desktop_config.json):
    {
        "mcpServers": {
            "nanobanana": {
                "command": "python",
                "args": ["/path/to/nanobanana_mcp.py"],
                "env": {
                    "GOOGLE_API_KEY": "your-api-key-here"
                }
            }
        }
    }
"""

import os
import base64
import json
from datetime import datetime
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent

# Initialize MCP server
server = Server("nanobanana")

# Model configurations
MODELS = {
    "pro": "gemini-3-pro-image-preview",
    "flash": "gemini-2.5-flash-image-preview"
}

ASPECT_RATIOS = ["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]

# Output directory for generated images
OUTPUT_DIR = Path.home() / "nanobanana_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def get_client():
    """Get the Google GenAI client."""
    try:
        from google import genai
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        return genai.Client(api_key=api_key)
    except ImportError:
        raise ImportError("google-genai package not installed. Run: pip install google-genai")


@server.list_tools()
async def list_tools():
    """List available Nanobanana tools."""
    return [
        Tool(
            name="nanobanana_generate",
            description="Generate an image using Nanobanana Pro (Gemini 3 Pro Image) API. Supports photorealistic images, creative art, infographics, and more.",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The image generation prompt. Be specific about style, lighting, composition, and details."
                    },
                    "aspect_ratio": {
                        "type": "string",
                        "description": "Image aspect ratio",
                        "enum": ASPECT_RATIOS,
                        "default": "16:9"
                    },
                    "model": {
                        "type": "string",
                        "description": "Model to use: 'pro' for Nanobanana Pro (4K, better quality) or 'flash' for Nanobanana Flash (faster, cheaper)",
                        "enum": ["pro", "flash"],
                        "default": "pro"
                    }
                },
                "required": ["prompt"]
            }
        ),
        Tool(
            name="nanobanana_edit",
            description="Edit an existing image using Nanobanana Pro. Supports background replacement, style transfer, object removal, outpainting, and virtual try-on.",
            inputSchema={
                "type": "object",
                "properties": {
                    "image_path": {
                        "type": "string",
                        "description": "Path to the input image file to edit"
                    },
                    "edit_instruction": {
                        "type": "string",
                        "description": "Instructions for how to edit the image (e.g., 'Change the background to a beach', 'Remove all people in the background')"
                    },
                    "aspect_ratio": {
                        "type": "string",
                        "description": "Output aspect ratio",
                        "enum": ASPECT_RATIOS,
                        "default": "1:1"
                    }
                },
                "required": ["image_path", "edit_instruction"]
            }
        ),
        Tool(
            name="nanobanana_multi_image",
            description="Generate an image using multiple reference images. Useful for combining subjects, virtual try-on, or style transfer.",
            inputSchema={
                "type": "object",
                "properties": {
                    "image_paths": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of paths to input images (up to 14 images supported)"
                    },
                    "prompt": {
                        "type": "string",
                        "description": "Instructions for combining the images (e.g., 'Create a group photo with all these people')"
                    },
                    "aspect_ratio": {
                        "type": "string",
                        "description": "Output aspect ratio",
                        "enum": ASPECT_RATIOS,
                        "default": "16:9"
                    }
                },
                "required": ["image_paths", "prompt"]
            }
        ),
        Tool(
            name="nanobanana_prompts",
            description="Get curated prompt examples from the awesome-nanobanana-pro collection for different use cases.",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Category of prompts to retrieve",
                        "enum": [
                            "photorealism",
                            "creative",
                            "ecommerce",
                            "productivity",
                            "social_media",
                            "editing",
                            "all"
                        ],
                        "default": "all"
                    }
                }
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    """Handle tool calls."""

    if name == "nanobanana_generate":
        return await generate_image(arguments)
    elif name == "nanobanana_edit":
        return await edit_image(arguments)
    elif name == "nanobanana_multi_image":
        return await multi_image_generate(arguments)
    elif name == "nanobanana_prompts":
        return await get_prompts(arguments)
    else:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def generate_image(arguments: dict):
    """Generate an image from a text prompt."""
    try:
        from google.genai import types

        client = get_client()
        prompt = arguments["prompt"]
        aspect_ratio = arguments.get("aspect_ratio", "16:9")
        model_key = arguments.get("model", "pro")
        model_id = MODELS[model_key]

        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image'],
                image_config=types.ImageConfig(
                    aspect_ratio=aspect_ratio,
                )
            )
        )

        results = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        for i, part in enumerate(response.parts):
            if image := part.as_image():
                filename = OUTPUT_DIR / f"nanobanana_{timestamp}_{i}.png"
                image.save(str(filename))
                results.append(f"Image saved to: {filename}")
            elif text := part.text:
                results.append(f"Response: {text}")

        return [TextContent(
            type="text",
            text=f"Generated image with prompt: '{prompt[:100]}...'\n\n" + "\n".join(results)
        )]

    except Exception as e:
        return [TextContent(type="text", text=f"Error generating image: {str(e)}")]


async def edit_image(arguments: dict):
    """Edit an existing image."""
    try:
        from google.genai import types

        client = get_client()
        image_path = arguments["image_path"]
        edit_instruction = arguments["edit_instruction"]
        aspect_ratio = arguments.get("aspect_ratio", "1:1")

        # Load the input image
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode()

        mime_type = "image/png" if image_path.endswith(".png") else "image/jpeg"

        response = client.models.generate_content(
            model=MODELS["pro"],
            contents=[
                {"inline_data": {"mime_type": mime_type, "data": image_data}},
                edit_instruction
            ],
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image'],
                image_config=types.ImageConfig(
                    aspect_ratio=aspect_ratio,
                )
            )
        )

        results = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        for i, part in enumerate(response.parts):
            if image := part.as_image():
                filename = OUTPUT_DIR / f"nanobanana_edit_{timestamp}_{i}.png"
                image.save(str(filename))
                results.append(f"Edited image saved to: {filename}")
            elif text := part.text:
                results.append(f"Response: {text}")

        return [TextContent(
            type="text",
            text=f"Edited image with instruction: '{edit_instruction[:100]}...'\n\n" + "\n".join(results)
        )]

    except Exception as e:
        return [TextContent(type="text", text=f"Error editing image: {str(e)}")]


async def multi_image_generate(arguments: dict):
    """Generate an image from multiple reference images."""
    try:
        from google.genai import types

        client = get_client()
        image_paths = arguments["image_paths"]
        prompt = arguments["prompt"]
        aspect_ratio = arguments.get("aspect_ratio", "16:9")

        contents = []
        for path in image_paths[:14]:  # Max 14 images
            with open(path, "rb") as f:
                image_data = base64.b64encode(f.read()).decode()
            mime_type = "image/png" if path.endswith(".png") else "image/jpeg"
            contents.append({"inline_data": {"mime_type": mime_type, "data": image_data}})

        contents.append(prompt)

        response = client.models.generate_content(
            model=MODELS["pro"],
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image'],
                image_config=types.ImageConfig(
                    aspect_ratio=aspect_ratio,
                )
            )
        )

        results = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        for i, part in enumerate(response.parts):
            if image := part.as_image():
                filename = OUTPUT_DIR / f"nanobanana_multi_{timestamp}_{i}.png"
                image.save(str(filename))
                results.append(f"Image saved to: {filename}")
            elif text := part.text:
                results.append(f"Response: {text}")

        return [TextContent(
            type="text",
            text=f"Generated image from {len(image_paths)} reference images\n\n" + "\n".join(results)
        )]

    except Exception as e:
        return [TextContent(type="text", text=f"Error generating image: {str(e)}")]


async def get_prompts(arguments: dict):
    """Get curated prompt examples."""
    category = arguments.get("category", "all")

    prompts = {
        "photorealism": {
            "Hyper-Realistic Portrait": "Create a hyper-realistic, ultra-sharp, full-color portrait. Photorealistic, 8k, shallow depth of field, soft natural fill light + strong golden rim light. High dynamic range, calibrated color grading. Skin tones perfectly accurate.",
            "Business Headshot": "Professional headshot, navy blue business suit, white shirt. Clean solid dark gray studio backdrop with subtle vignette. Shot on Sony A7III with 85mm f/1.4 lens. Three-point lighting setup. Natural skin texture with visible pores.",
            "Film Photography": "Cinematic portrait shot on Kodak Portra 400 film. Urban coffee shop at Golden Hour. Warm, nostalgic lighting. Subtle film grain and soft focus for dreamy vibe."
        },
        "creative": {
            "Recursive Image": "Recursive image of an orange cat sitting in an office chair holding up an iPad. On the iPad is the same cat in the same scene holding up the same iPad. Repeated on each iPad.",
            "Coordinate Visualization": "35.6586° N, 139.7454° E at 19:00",
            "Aging Effect": "Generate the holiday photo of this person through the ages up to 80 years old",
            "Whiteboard Art": "Create a photo of vagabonds musashi praying drawn on a glass whiteboard in a slightly faded green marker"
        },
        "ecommerce": {
            "Virtual Try-On": "Using Image 1 (the garment) and Image 2 (the model), create a hyper-realistic full-body fashion photo. The garment must drape naturally, creating realistic folds and wrinkles. Preserve original fabric texture, color, and logos.",
            "Product Photography": "Identify the main product, remove hands/clutter. Premium e-commerce shot on pure white background (RGB 255,255,255) with subtle contact shadow. Soft commercial studio lighting."
        },
        "productivity": {
            "Flowchart Conversion": "Convert this hand-drawn sketch into professional corporate flowchart. McKinsey-style: clean lines, ample whitespace, blue-and-gray palette. Align to strict grid, orthogonal arrows.",
            "UI Prototype": "Transform wireframe sketch into high-fidelity UI mockup. Modern iOS 18 aesthetic. Rounded corners, soft shadows, vibrant primary color. Place inside iPhone 16 frame."
        },
        "social_media": {
            "Viral Thumbnail": "Design viral video thumbnail. Excited expression, person pointing towards subject. Bold yellow arrow, massive pop-style text with white outline. High saturation and contrast.",
            "Promotional Poster": "Professional promotional poster. Cinematic close-up with steaming product. Elegant gold serif typography. Offer badge/sticker style. All text perfectly spelled and centered."
        },
        "editing": {
            "Smart Outpainting": "Zoom out and expand to 16:9 aspect ratio. Seamlessly extend scenery, matching original lighting, weather, and texture perfectly.",
            "Crowd Removal": "Remove all tourists/people in background. Replace with realistic background elements. No blurry artifacts. Same grain, focus depth, and lighting.",
            "Translation": "Translate text to English. Maintain original aged/textured surface look. Keep currency symbols and prices. Align translations naturally."
        }
    }

    if category == "all":
        result = json.dumps(prompts, indent=2)
    elif category in prompts:
        result = json.dumps({category: prompts[category]}, indent=2)
    else:
        result = "Category not found. Available: " + ", ".join(prompts.keys())

    return [TextContent(type="text", text=result)]


async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
