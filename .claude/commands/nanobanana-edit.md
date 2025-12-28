# Nanobanana Image Editing

Edit images using the Nanobanana Pro (Gemini 3 Pro Image) API.

## Usage
When the user wants to edit an existing image, help them create and execute Python code using the Nanobanana API.

## Requirements
- Google API Key (set as `GOOGLE_API_KEY` environment variable)
- Python with `google-genai` package installed (`pip install google-genai`)
- Input image file

## API Details
- **Model**: `gemini-3-pro-image-preview` (recommended for editing)
- **Capabilities**: Background replacement, style transfer, object removal, outpainting, virtual try-on

## Code Template

```python
import os
import base64
from google import genai
from google.genai import types

# Initialize the client
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

MODEL_ID = "gemini-3-pro-image-preview"

# Load the input image
input_image_path = "INPUT_IMAGE_PATH"  # Replace with actual path
with open(input_image_path, "rb") as f:
    image_data = base64.b64encode(f.read()).decode()

# Determine mime type
mime_type = "image/png" if input_image_path.endswith(".png") else "image/jpeg"

# User's editing instruction
edit_prompt = """$ARGUMENTS"""

# Generate the edited image
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        {"inline_data": {"mime_type": mime_type, "data": image_data}},
        edit_prompt
    ],
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image'],
        image_config=types.ImageConfig(
            aspect_ratio="1:1",  # Adjust as needed
        )
    )
)

# Save the edited image
for i, part in enumerate(response.parts):
    if image := part.as_image():
        filename = f"nanobanana_edited_{i}.png"
        image.save(filename)
        print(f"Edited image saved to: {filename}")
    elif text := part.text:
        print(f"Response: {text}")
```

## Common Editing Tasks (from awesome-nanobanana-pro)

### Virtual Try-On
```
Using Image 1 (the garment) and Image 2 (the model), create a hyper-realistic full-body fashion photo where the model is wearing the garment. The garment must drape naturally, preserving fabric texture and logos.
```

### Smart Outpainting
```
Zoom out and expand this image to a 16:9 aspect ratio. Seamlessly extend the scenery, matching original lighting, weather, and texture perfectly.
```

### Crowd Removal
```
Remove all the tourists/people in the background behind the main subject. Replace with realistic background elements that logically fit the scene.
```

### Style Transfer
```
Without changing her original face, create a portrait in 1990s-style camera using direct front flash. 35mm lens flash creates a nostalgic glow.
```

Help the user specify their input image and editing instructions.
