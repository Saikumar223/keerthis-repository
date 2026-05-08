def generate_image_prompts(scenes):

    prompts = []

    base_style = (
        "Ultra realistic Hyderabad intermediate student girl, "
        "natural South Indian appearance, "
        "android selfie camera realism, "
        "middle class room, "
        "realistic skin texture, "
        "natural lighting"
    )

    for scene in scenes:

        full_prompt = (
            f"{base_style}, "
            f"{scene['description']}"
        )

        prompts.append({
            "scene_number": scene["scene_number"],
            "prompt": full_prompt
        })

    return prompts
