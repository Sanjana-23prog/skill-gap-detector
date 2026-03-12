import pandas as pd

def find_missing_skills(user_skills, role):
    
    # load dataset
    df = pd.read_csv("dataset.csv")

    # get required skills for the role
    role_data = df[["skill", role]]

    required_skills = role_data["skill"].tolist()

    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in [s.lower() for s in user_skills]:
            missing_skills.append(skill)

    return missing_skills
