from story_memory import get_story_memory


def generate_caption(parsed_data):

    theme = parsed_data["theme"]
    mood = parsed_data["mood"]
    memory = get_story_memory()

    if theme == "EAMCET preparation":
        return (
            "5 mins break ani reel chestunna 😭 "
            "#EAMCET #StudentLife"
        )

    if theme == "exam stress":
        return (
            f"{memory['current_emotion']} but still trying my best 💀"
        )

    if mood == "emotional":
        return (
            "Konni rojulu stress ekkuva untundi… but we keep going ✨"
        )

    return (
        f"{memory['current_stage']} life ante survive avvadame ✨"
    )