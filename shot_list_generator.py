def generate_shot_list(scenes):

    shot_types = [
        "Close-up selfie shot",
        "Study table medium shot",
        "Rainy window cinematic shot",
        "Over-the-shoulder study shot",
        "Natural handheld mobile shot"
    ]

    lines = []

    for index, scene in enumerate(scenes):
        shot = shot_types[index % len(shot_types)]

        lines.append(
            f"Scene {scene['scene_number']}: "
            f"{shot} - "
            f"{scene['description']}"
        )

    return "\n".join(lines)