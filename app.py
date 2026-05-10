import json

from prompt_parser import parse_prompt
from scene_generator import generate_scenes
from image_prompt_generator import generate_image_prompts
from caption_generator import generate_caption


def generate_reel(prompt):

    parsed_data = parse_prompt(prompt)

    scenes = generate_scenes(parsed_data)

    image_prompts = generate_image_prompts(scenes)

    caption = generate_caption(parsed_data)

    final_output = {
        "parsed_data": parsed_data,
        "scenes": scenes,
        "image_prompts": image_prompts,
        "caption": caption
    }

    print("\n")
    print(json.dumps(final_output, indent=4))
    print("\n")


def main():

    print("=== Keerthi Story Engine ===")
    print("Type 'exit' anytime to stop.\n")

    while True:

        user_prompt = input("Enter Reel Idea: ")

        if user_prompt.lower() == "exit":
            print("Exiting Keerthi Engine...")
            break

        generate_reel(user_prompt)


if __name__ == "__main__":
    main()