import json


def generate_asset_manifest(final_output):

    manifest = {
        "character": "Keerthi",
        "scene_count": len(final_output["scenes"]),
        "deliverables": [
            "reel_output.json",
            "caption.txt",
            "image_prompts.txt",
            "video_script.txt",
            "shot_list.txt",
            "production_plan.md",
            "checklist.md"
        ],
        "recommended_tools": {
            "image_generation": "ChatGPT Images / Leonardo AI",
            "video_animation": "Kling AI / Runway ML",
            "editing": "CapCut"
        }
    }

    return json.dumps(manifest, indent=4, ensure_ascii=False)