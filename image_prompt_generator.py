import random


def generate_image_prompts(scenes):

    prompts = []

    camera_styles = [
        "android front camera selfie realism",
        "natural handheld mobile camera shot",
        "Instagram reel style camera angle",
        "casual smartphone photography",
        "realistic student vlog style"
    ]

    lighting_styles = [
        "soft natural lighting",
        "rainy evening lighting",
        "warm study lamp lighting",
        "realistic indoor middle class room lighting",
        "natural window light"
    ]

    aesthetic_styles = [
        "natural skin texture",
        "slightly messy realistic student room",
        "authentic Hyderabad middle class home",
        "realistic South Indian teenage appearance",
        "casual home atmosphere"
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
            f"Ultra realistic Hyderabad intermediate student girl, "
            f"{random.choice(camera_styles)}, "
            f"{random.choice(lighting_styles)}, "
            f"{random.choice(aesthetic_styles)}, "
            f"{random.choice(emotion_styles)}, "
            f"{scene['description']}"
        )

        prompts.append({
            "scene_number": scene["scene_number"],
            "prompt": full_prompt
        })

    return prompts