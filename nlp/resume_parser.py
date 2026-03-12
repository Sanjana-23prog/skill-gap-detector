import re

def extract_skills_from_resume(text):

    # predefined skill list
    skills_list = [
        "python",
        "sql",
        "machine learning",
        "ml",
        "data analysis",
        "git",
        "dsa"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills
