import json
import os
from datetime import datetime


OUTPUT_DIR = "outputs"


def _create_run_folder():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_folder = os.path.join(OUTPUT_DIR, timestamp)

    os.makedirs(run_folder, exist_ok=True)
    os.makedirs(os.path.join(run_folder, "prompts"), exist_ok=True)
    os.makedirs(os.path.join(run_folder, "generated_images"), exist_ok=True)

    return run_folder


def _write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def _create_prompt_files(run_folder, image_prompts):
    prompts_folder = os.path.join(run_folder, "prompts")

    for item in image_prompts:
        scene_number = item["scene_number"]

        file_path = os.path.join(
            prompts_folder,
            f"scene_{scene_number}_prompt.txt"
        )

        _write(file_path, item["prompt"])


def _create_image_placeholders(run_folder, image_prompts):
    images_folder = os.path.join(run_folder, "generated_images")

    for item in image_prompts:
        scene_number = item["scene_number"]

        placeholder_path = os.path.join(
            images_folder,
            f"scene_{scene_number}.png"
        )

        # Create an empty placeholder file only if it doesn't exist.
        if not os.path.exists(placeholder_path):
            with open(placeholder_path, "wb"):
                pass


def save_all_outputs(final_output):

    run_folder = _create_run_folder()

    # Save structured JSON
    with open(
        os.path.join(run_folder, "reel_output.json"),
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(final_output, f, indent=4, ensure_ascii=False)

    # Save standard text outputs
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

    # Save combined image prompts
    with open(
        os.path.join(run_folder, "image_prompts.txt"),
        "w",
        encoding="utf-8"
    ) as f:
        for item in final_output["image_prompts"]:
            f.write(f"Scene {item['scene_number']}\n")
            f.write(item["prompt"])
            f.write("\n\n")

    # Save one prompt file per scene
    _create_prompt_files(
        run_folder,
        final_output["image_prompts"]
    )

    # Create placeholder image files
    _create_image_placeholders(
        run_folder,
        final_output["image_prompts"]
    )

    return run_folder