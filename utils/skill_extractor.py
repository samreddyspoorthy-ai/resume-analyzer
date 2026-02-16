import json

def extract_skills(text):
    with open("data/skills_list.json") as f:
        skills = json.load(f)

    found = []
    for skill in skills:
        if skill.lower() in text.lower():
            found.append(skill)

    return found
