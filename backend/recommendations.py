import json

def recommend_projects(missing_skills):

    with open("data/projects.json") as f:
        projects = json.load(f)

    suggestions = []

    for skill in missing_skills:
        if skill.lower() in projects:
            suggestions.extend(projects[skill.lower()])

    return suggestions
