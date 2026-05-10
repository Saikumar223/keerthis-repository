import random


def generate_scenes(parsed_data):

    theme = parsed_data["theme"]
    mood = parsed_data["mood"]
    weather = parsed_data["weather"]

    intro_scenes = [
        "Keerthi studying with messy notes and tired eyes",
        "Keerthi sitting near study table stressed about exams",
        "Keerthi solving physics problems with frustrated expression",
        "Keerthi revising chemistry formulas late night"
    ]

    stress_relief_scenes = [
        "Keerthi checking mobile during study break",
        "Keerthi casually scrolling Instagram while studying",
        "Keerthi relaxing after continuous studying",
        "Keerthi taking small break while preparing for exams"
    ]

    rainy_scenes = [
        "Keerthi drinking chai near rainy window",
        "Keerthi watching rain while listening to songs",
        "Keerthi enjoying cool weather from balcony",
        "Keerthi relaxing during rainy evening study break"
    ]

    emotional_scenes = [
        "Keerthi feeling emotionally tired while studying late night",
        "Keerthi silently thinking about future and exams",
        "Keerthi staring at books feeling overwhelmed",
        "Keerthi sitting quietly after mock test stress"
    ]

    motivational_scenes = [
        "Keerthi motivating herself to continue studying",
        "Keerthi restarting preparation with determination",
        "Keerthi trying hard despite stress and pressure"
    ]

    ending_scenes = [
        "Keerthi returning to study after short relaxation",
        "Keerthi realizing too much time passed during break",
        "Keerthi feeling guilty for taking long break",
        "Keerthi continuing EAMCET preparation seriously"
    ]

    scenes = []

    # Intro
    scenes.append({
        "scene_number": 1,
        "description": random.choice(intro_scenes)
    })

    # Mood Layer
    if mood == "stress relief":

        scenes.append({
            "scene_number": 2,
            "description": random.choice(stress_relief_scenes)
        })

    if mood == "emotional":

        scenes.append({
            "scene_number": 3,
            "description": random.choice(emotional_scenes)
        })

    # Weather Layer
    if weather == "rainy":

        scenes.append({
            "scene_number": 4,
            "description": random.choice(rainy_scenes)
        })

    # Motivation Layer
    scenes.append({
        "scene_number": 5,
        "description": random.choice(motivational_scenes)
    })

    # Ending
    scenes.append({
        "scene_number": 6,
        "description": random.choice(ending_scenes)
    })

    return scenes