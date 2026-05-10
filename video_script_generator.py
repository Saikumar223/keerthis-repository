def generate_video_script(parsed_data, scenes):

    lines = []

    theme = parsed_data.get("theme", "")

    if theme == "EAMCET preparation":
        lines.append(
            "Intermediate second year life ante books, pressure, and small breaks in between."
        )
    else:
        lines.append(
            "Every day has a story, and every small moment matters."
        )

    for scene in scenes:
        lines.append(scene["description"])

    lines.append(
        "No matter how stressful life gets, we keep moving forward."
    )

    return "\n".join(lines)