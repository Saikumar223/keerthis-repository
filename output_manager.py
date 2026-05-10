import json
import os
from datetime import datetime


OUTPUT_DIR = "outputs"


def _create_run_folder():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_folder = os.path.join(OUTPUT_DIR, timestamp)

    os.makedirs(run_folder, exist_ok=True)

    return run_folder


def _write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def save_all_outputs(final_output):

    run_folder = _create_run_folder()

    # Save structured JSON
    with open(
        os.path.join(run_folder, "reel_output.json"),
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(final_output, f, indent=4, ensure_ascii=False)

    # Save text-based outputs
    text_files = {
        "caption.txt": final_output["caption"],
        "video_script.txt": final_output["video_script"],
        "shot_list.txt": final_output["shot_list"],
        "production_plan.md": final_output["production_plan"],
        "asset_manifest.json": final_output["asset_manifest"],
        "checklist.md": final_output["checklist"]
    }

    for filename, content in text_files.items():
        _write(os.path.join(run_folder, filename), content)

    # Save image prompts
    with open(
        os.path.join(run_folder, "image_prompts.txt"),
        "w",
        encoding="utf-8"
    ) as f:
        for item in final_output["image_prompts"]:
            f.write(f"Scene {item['scene_number']}\n")
            f.write(item["prompt"])
            f.write("\n\n")

    return run_folder