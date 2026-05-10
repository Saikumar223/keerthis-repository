def generate_production_plan(final_output):

    caption = final_output["caption"]

    lines = [
        "# Keerthi Reel Production Plan",
        "",
        "## Caption",
        caption,
        "",
        "## Workflow",
        "1. Generate images using image_prompts.txt",
        "2. Use the reference portrait for face consistency",
        "3. Animate images using Kling AI or Runway ML",
        "4. Use video_script.txt as voiceover",
        "5. Follow shot_list.txt for camera style",
        "6. Assemble everything in CapCut",
        "",
        "## Deliverables",
        "- Instagram Reel (9:16)",
        "- Thumbnail",
        "- Caption and hashtags"
    ]

    return "\n".join(lines)