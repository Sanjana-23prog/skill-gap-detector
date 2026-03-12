def calculate_readiness(user_skills, required_skills):

    matched = len(set(user_skills) & set(required_skills))

    total = len(required_skills)

    score = (matched / total) * 100

    return round(score, 2)
