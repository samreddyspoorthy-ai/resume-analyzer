import json

def extract_skills(text):
    with open("data/skills_list.json") as f:
        skills = json.load(f)

    text = text.lower()

    found = [skill for skill in skills if skill.lower() in text]

    return list(set(found))
