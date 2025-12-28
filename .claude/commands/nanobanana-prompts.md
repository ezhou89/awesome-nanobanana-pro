# Nanobanana Prompt Library

Browse and use curated prompts from the awesome-nanobanana-pro collection.

## Categories

### 1. Photorealism & Aesthetics

**Hyper-Realistic Crowd Composition**
```
Create a hyper-realistic, ultra-sharp, full-color large-format image featuring a massive group of celebrities from different eras. Photorealistic, 8k, shallow depth of field, soft natural fill light + strong golden rim light. High dynamic range, calibrated color grading. Skin tones perfectly accurate.
```

**2000s Mirror Selfie** (JSON format)
```json
{
  "subject": {
    "description": "A young woman taking a mirror selfie with very long voluminous dark waves",
    "expression": "confident and slightly playful"
  },
  "photography": {
    "camera_style": "early-2000s digital camera aesthetic",
    "lighting": "harsh super-flash with bright blown-out highlights",
    "texture": "subtle grain, retro highlights, V6 realism"
  },
  "background": {
    "setting": "nostalgic early-2000s bedroom",
    "elements": ["CD player", "posters of 2000s pop icons", "beaded door curtain"]
  }
}
```

**Professional Business Headshot**
```
Keep facial features exactly consistent. Navy blue business suit, white shirt. Clean solid dark gray studio backdrop with subtle vignette. Shot on Sony A7III with 85mm f/1.4 lens. Three-point lighting setup. Natural skin texture with visible pores. 8k professional headshot.
```

### 2. Creative Experiments

**Recursive/Droste Effect**
```
Recursive image of an orange cat sitting in an office chair holding up an iPad. On the iPad is the same cat in the same scene holding up the same iPad. Repeated on each iPad.
```

**Coordinate Visualization**
```
35.6586° N, 139.7454° E at 19:00
```

**Aging Through Years**
```
Generate the holiday photo of this person through the ages up to 80 years old
```

### 3. E-commerce & Product

**Product Photography**
```
Identify the main product, removing any hands or clutter. Recreate as premium e-commerce shot. Pure white studio background (RGB 255,255,255) with subtle contact shadow. Soft commercial studio lighting. Fix lens distortion, improve sharpness.
```

### 4. Design & Productivity

**Flowchart Conversion**
```
Convert this hand-drawn sketch into professional corporate flowchart. Minimalist McKinsey-style: clean lines, ample whitespace, blue-and-gray palette. Align to strict grid, orthogonal arrows. Clear Sans-Serif font.
```

**UI Prototype**
```
Transform this wireframe sketch into high-fidelity UI mockup for mobile app. Modern iOS 18 or Material Design 3 aesthetic. Rounded corners, soft shadows, vibrant primary color. Place inside realistic iPhone 16 frame.
```

### 5. Social Media

**Viral Thumbnail**
```
Design viral video thumbnail. Keep facial features exact but change expression to excited and surprised. Person pointing towards subject on right. Add bold yellow arrow, massive pop-style text with white outline and drop shadow. High saturation and contrast.
```

## Usage

1. Copy any prompt above
2. Use `/nanobanana-generate [prompt]` to generate
3. Use `/nanobanana-edit [instructions]` for image editing
4. Customize prompts for your specific needs

## Tips

- Be specific about lighting, camera settings, and style
- Use JSON format for complex structured prompts
- Reference specific eras or styles (1990s camera, 2000s aesthetic)
- Include technical details (lens, f-stop, resolution)
- Specify aspect ratio in your generation config
