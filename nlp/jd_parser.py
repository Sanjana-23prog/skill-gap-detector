def extract_skills_from_job_description(text):

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

    required_skills = []

    for skill in skills_list:
        if skill in text:
            required_skills.append(skill)

    return required_skills
