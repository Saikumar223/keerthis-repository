import json

from prompt_parser import parse_prompt
from scene_generator import generate_scenes
from image_prompt_generator import generate_image_prompts
from caption_generator import generate_caption
from video_script_generator import generate_video_script
from shot_list_generator import generate_shot_list
from production_plan_generator import generate_production_plan
from asset_manifest_generator import generate_asset_manifest
from checklist_generator import generate_checklist
from output_manager import save_all_outputs


def generate_reel(prompt):

    parsed_data = parse_prompt(prompt)
    scenes = generate_scenes(parsed_data)
    image_prompts = generate_image_prompts(scenes)
    caption = generate_caption(parsed_data)
    video_script = generate_video_script(parsed_data, scenes)
    shot_list = generate_shot_list(scenes)

    final_output = {
        "input_prompt": prompt,
        "parsed_data": parsed_data,
        "scenes": scenes,
        "image_prompts": image_prompts,
        "caption": caption,
        "video_script": video_script
    }

    final_output["shot_list"] = shot_list
    final_output["production_plan"] = generate_production_plan(final_output)
    final_output["asset_manifest"] = generate_asset_manifest(final_output)
    final_output["checklist"] = generate_checklist()

    print("\\n")
    print(json.dumps(final_output, indent=4, ensure_ascii=False))
    print("\\n")

    output_folder = save_all_outputs(final_output)

    print(f"All outputs saved to: {output_folder}\\n")


def main():

    print("=== Keerthi Story Engine V7 ===")
    print("Type 'exit' anytime to stop.\\n")

    while True:

        user_prompt = input("Enter Reel Idea: ")

        if user_prompt.lower() == "exit":
            print("Exiting Keerthi Engine...")
            break

        if not user_prompt.strip():
            print("Please enter a valid prompt.\\n")
            continue

        generate_reel(user_prompt)


if __name__ == "__main__":
    main()