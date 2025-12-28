# Nanobanana Image Generation

Generate images using the Nanobanana Pro (Gemini 3 Pro Image) API.

## Usage
When the user provides an image generation request, help them create and execute Python code to generate images using the Nanobanana API.

## Requirements
- Google API Key (set as `GOOGLE_API_KEY` environment variable or passed directly)
- Python with `google-genai` package installed (`pip install google-genai`)

## API Details
- **Model**: `gemini-3-pro-image-preview` (Nanobanana Pro) or `gemini-2.5-flash-image-preview` (Nanobanana Flash)
- **Supported Aspect Ratios**: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`
- **Max Resolution**: Up to 4K

## Code Template

```python
import os
from google import genai
from google.genai import types

# Initialize the client
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Model selection
MODEL_ID = "gemini-3-pro-image-preview"  # Pro version (4K, search grounding)
# MODEL_ID = "gemini-2.5-flash-image-preview"  # Flash version (faster, cheaper)

# User's prompt
prompt = """$ARGUMENTS"""

# Generate the image
response = client.models.generate_content(
    model=MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image'],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",  # Change as needed
        )
    )
)

# Save the generated image
for i, part in enumerate(response.parts):
    if image := part.as_image():
        filename = f"nanobanana_output_{i}.png"
        image.save(filename)
        print(f"Image saved to: {filename}")
    elif text := part.text:
        print(f"Response: {text}")
```

## Example Prompts (from awesome-nanobanana-pro)

1. **Photorealistic Portrait**: "Create a hyper-realistic portrait with 8k quality, shallow depth of field, soft natural fill light"
2. **Retro Aesthetic**: "Create a 2000s mirror selfie with harsh flash, nostalgic bedroom background"
3. **Business Headshot**: "Professional headshot, navy blue suit, dark gray studio backdrop, Canon EOS R5 with 85mm f/1.4 lens"
4. **Creative**: "A where is waldo image showing all Star Wars characters on Tatooine"

Help the user craft their prompt and execute the generation code.
