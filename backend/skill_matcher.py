import pandas as pd

def get_required_skills(role):
    df = pd.read_csv("dataset.csv")
    skills = df["skill"].tolist()
    return skills


def find_missing_skills(user_skills, role):

    required_skills = get_required_skills(role)

    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in [s.lower() for s in user_skills]:
            missing_skills.append(skill)

    return missing_skills
