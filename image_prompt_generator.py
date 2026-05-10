import random

from character_profile import get_character_profile


def generate_image_prompts(scenes):

    prompts = []
    profile = get_character_profile()

    appearance = profile["appearance"]
    room_details = profile["room_details"]
    social_style = profile["social_style"]

    # Core character description (used in every prompt)
    base_character = (
        f"{profile['name']}, "
        f"{profile['age']} year old Hyderabad intermediate second year MPC student, "
        f"{appearance['skin_tone']}, "
        f"{appearance['hair']}, "
        f"{appearance['eyes']}, "
        f"{appearance['style']}"
    )

    # Use first few room details to keep prompts concise
    room_context = ", ".join(room_details[:5])

    camera_styles = [
        "android front camera selfie realism",
        "natural handheld mobile camera shot",
        "Instagram reel style camera angle",
        "casual smartphone photography",
        "realistic student vlog style"
    ]

    lighting_styles = [
        "soft natural daylight",
        "rainy evening lighting",
        "warm study lamp lighting",
        "realistic indoor middle class room lighting",
        "natural window light"
    ]

    emotion_styles = [
        "emotionally relatable expression",
        "natural facial emotions",
        "realistic tired student face",
        "subtle cinematic emotion",
        "genuine human expression"
    ]

    for scene in scenes:

        full_prompt = (
            f"Ultra realistic portrait of {base_character}, "
            f"{room_context}, "
            f"{random.choice(camera_styles)}, "
            f"{random.choice(lighting_styles)}, "
            f"{random.choice(emotion_styles)}, "
            f"{random.choice(social_style)}, "
            f"Reference image: {profile['reference_image']}, "
            f"{scene['description']}"
        )

        prompts.append({
            "scene_number": scene["scene_number"],
            "prompt": full_prompt,
            "reference_image": profile["reference_image"]
        })

    return prompts