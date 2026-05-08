def parse_prompt(user_prompt):

    prompt_lower = user_prompt.lower()

    parsed_data = {
        "character": "Keerthi",
        "theme": "student life",
        "mood": "relatable",
        "location": "study room",
        "weather": "normal"
    }

    if "eamcet" in prompt_lower:
        parsed_data["theme"] = "EAMCET preparation"

    if "rain" in prompt_lower:
        parsed_data["weather"] = "rainy"
        parsed_data["mood"] = "emotional"

    if "break" in prompt_lower:
        parsed_data["mood"] = "stress relief"

    if "exam" in prompt_lower:
        parsed_data["theme"] = "exam stress"

    return parsed_data
