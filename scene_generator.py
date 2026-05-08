def generate_scenes(parsed_data):

    theme = parsed_data["theme"]

    if theme == "EAMCET preparation":

        scenes = [
            {
                "scene_number": 1,
                "description": "Keerthi studying physics with messy notes and tired expression"
            },
            {
                "scene_number": 2,
                "description": "Keerthi taking mobile during study break"
            },
            {
                "scene_number": 3,
                "description": "Keerthi drinking chai near rainy window while relaxing"
            },
            {
                "scene_number": 4,
                "description": "Keerthi realizing too much break time passed and returning to study"
            }
        ]

        return scenes

    return [
        {
            "scene_number": 1,
            "description": "Keerthi casually sitting in her room"
        }
    ]
