# Nanobanana MCP Server

An MCP (Model Context Protocol) server that provides Nanobanana Pro (Gemini 3 Pro Image) API integration for Claude Desktop and other MCP clients.

## Features

- **Image Generation**: Generate images from text prompts with configurable aspect ratios
- **Image Editing**: Edit existing images with natural language instructions
- **Multi-Image Compositing**: Combine up to 14 reference images
- **Curated Prompts**: Access a library of proven prompts from awesome-nanobanana-pro

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Google API key:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## Claude Desktop Configuration

Add this to your `claude_desktop_config.json`:

### macOS
Location: `~/Library/Application Support/Claude/claude_desktop_config.json`

### Windows
Location: `%APPDATA%\Claude\claude_desktop_config.json`

### Configuration
```json
{
  "mcpServers": {
    "nanobanana": {
      "command": "python",
      "args": ["/path/to/mcp-server/nanobanana_mcp.py"],
      "env": {
        "GOOGLE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Available Tools

### `nanobanana_generate`
Generate an image from a text prompt.

**Parameters:**
- `prompt` (required): The image generation prompt
- `aspect_ratio`: One of `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
- `model`: `pro` (4K, better quality) or `flash` (faster, cheaper)

**Example:**
```
Generate a hyper-realistic portrait with 8k quality, shallow depth of field,
soft natural fill light. Professional headshot style.
```

### `nanobanana_edit`
Edit an existing image using natural language.

**Parameters:**
- `image_path` (required): Path to the input image
- `edit_instruction` (required): How to modify the image
- `aspect_ratio`: Output aspect ratio

**Example:**
```
Remove all people in the background and replace with a sunset beach scene.
```

### `nanobanana_multi_image`
Combine multiple reference images into one.

**Parameters:**
- `image_paths` (required): List of up to 14 image paths
- `prompt` (required): Instructions for combining images
- `aspect_ratio`: Output aspect ratio

**Example:**
```
Create a team photo with all these people, everyone making a silly face.
```

### `nanobanana_prompts`
Get curated prompt examples.

**Parameters:**
- `category`: One of `photorealism`, `creative`, `ecommerce`, `productivity`, `social_media`, `editing`, `all`

## Output

Generated images are saved to `~/nanobanana_outputs/` with timestamps.

## Model Information

- **Nanobanana Pro** (`gemini-3-pro-image-preview`): Best quality, 4K output, search grounding
- **Nanobanana Flash** (`gemini-2.5-flash-image-preview`): Faster and more cost-effective

## Resources

- [awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) - Curated prompts collection
- [Google AI Studio](https://aistudio.google.com/) - Get your API key
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs/image-generation)
