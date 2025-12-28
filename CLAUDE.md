# CLAUDE.md - AI Assistant Guide

This document provides guidance for AI assistants working with the **Awesome Nano Banana Pro** repository.

## Repository Overview

This is an "Awesome List" style repository containing a curated collection of high-quality prompts for AI image generation using the Nano Banana Pro model. The repository focuses on photorealistic portraits, stylized aesthetics, and creative visual experiments.

### Project Type
- **Category**: Curated resource collection (Awesome List)
- **Content**: AI image generation prompts
- **License**: MIT License
- **Primary File**: `README.md` (contains all prompts and documentation)

## Repository Structure

```
awesome-nanobanana-pro/
├── README.md      # Main content file with all prompts organized by category
├── LICENSE        # MIT License
└── CLAUDE.md      # This file - AI assistant guidance
```

## Content Organization

The README.md is organized into the following categories:

1. **Photorealism & Aesthetics** - High-fidelity portrait and photography prompts
2. **Creative Experiments** - Experimental compositions and visual effects
3. **Education & Knowledge** - Educational infographic generation
4. **E-commerce & Virtual Studio** - Product photography and virtual try-on
5. **Workplace & Productivity** - Flowcharts, UI mockups, layouts
6. **Photo Editing & Restoration** - Outpainting, object removal
7. **Interior Design** - Floor plan to design visualization
8. **Social Media & Marketing** - Thumbnails, promotional posters
9. **Daily Life & Translation** - Visual translation and localization
10. **Social Networking & Avatars** - Avatar and sticker creation
11. **Resources** - External links and documentation
12. **Contributing** - Contribution guidelines

## Conventions and Standards

### Prompt Entry Format

Each prompt entry follows this consistent format:

```markdown
### X.Y. Title of Prompt
*Brief description of the prompt's purpose and capabilities.*
<img width="XXX" alt="Description" src="image_url" />

**Prompt:**
```text or ```json
[The actual prompt content]
```
*Source: [@username](url) or [Platform](url)*
```

### Key Conventions

1. **Numbering**: Use hierarchical numbering (e.g., 1.1, 1.2, 2.1)
2. **Source Attribution**: Always include source links to credit original creators
3. **Image Dimensions**: Specify width/height in image tags for consistency
4. **Code Blocks**: Use `text` or `json` language hints for prompt code blocks
5. **Descriptions**: Include italic descriptions explaining the prompt's purpose

### Image Guidelines

- Use GitHub user-attachments for images when possible
- Include descriptive alt text for accessibility
- Specify dimensions (width/height attributes)
- For comparison images, use side-by-side layouts with `<p align="center">`

## Development Workflow

### Adding a New Prompt

1. Identify the appropriate category from the Table of Contents
2. Determine the next available subsection number
3. Add the prompt following the standard format:
   - Title with hierarchical number
   - Italicized description
   - Sample image(s)
   - The prompt in a code block
   - Source attribution with link

### Making Changes

1. Fork the repository
2. Create a new branch
3. Make changes following the established format
4. Submit a Pull Request

### Quality Standards

When adding prompts, ensure:
- The prompt is tested and produces good results
- The source/creator is properly credited
- Images demonstrate the prompt's output quality
- The description clearly explains the use case

## AI Assistant Guidelines

### When Working on This Repository

1. **Preserve Structure**: Maintain the existing markdown formatting and hierarchy
2. **Respect Attribution**: Never remove or modify source credits
3. **Follow Numbering**: Continue the hierarchical numbering scheme when adding content
4. **Image Handling**: Keep existing image references intact; add new images following the same patterns
5. **Category Placement**: Place new prompts in the most appropriate existing category

### Common Tasks

- **Adding Prompts**: Follow the entry format exactly, including source attribution
- **Updating Content**: Preserve formatting, only modify the specific content requested
- **Reorganizing**: Maintain Table of Contents sync with actual sections
- **Fixing Links**: Verify links work before and after changes

### What to Avoid

- Don't renumber existing sections unless specifically requested
- Don't remove source attributions
- Don't change the fundamental structure without explicit request
- Don't add categories without updating the Table of Contents

## Metadata

- **Last Updated**: Check the date at the top of README.md
- **Original Author**: ZeroLu
- **Repository Style**: Follows the [Awesome List](https://github.com/sindresorhus/awesome) format

## Quick Reference

| Task | Action |
|------|--------|
| Add new prompt | Find category → Add numbered entry → Include image + prompt + source |
| Update prompt | Locate by number → Edit content → Preserve format |
| Fix formatting | Match surrounding entries → Use consistent markdown |
| Add category | Create section → Update Table of Contents → Add to correct position |
