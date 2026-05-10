import json

from character_profile import get_character_profile


def generate_asset_manifest(final_output):

    profile = get_character_profile()

    manifest = {
        "character": profile["name"],
        "reference_image": profile["reference_image"],
        "scene_count": len(final_output["scenes"]),
        "deliverables": [
            "reel_output.json",
            "caption.txt",
            "image_prompts.txt",
            "video_script.txt",
            "shot_list.txt",
            "production_plan.md",
            "asset_manifest.json",
            "checklist.md"
        ],
        "recommended_tools": {
            "image_generation": "ChatGPT Images",
            "video_animation": "Kling AI or Runway ML",
            "editing": "CapCut"
        },
        "notes": [
            "Use the reference_image to maintain Keerthi's face across all future scenes.",
            "Generate one image per scene using image_prompts.txt.",
            "Animate the images and combine them into a 9:16 Instagram reel."
        ]
    }

    return json.dumps(manifest, indent=4, ensure_ascii=False)