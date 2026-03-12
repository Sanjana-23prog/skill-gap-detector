import streamlit as st
import pandas as pd
from backend.skill_matcher import find_missing_skills
from backend.readiness_score import readiness_score

st.title("Skill Gap Detector")

st.write("Analyze your skills and compare with industry requirements.")

# Select job role
role = st.selectbox(
    "Select your target job role",
    ["Software Engineer", "Data Analyst", "AI Engineer"]
)

# Enter user skills
skills_input = st.text_input(
    "Enter your skills separated by commas (example: Python, SQL, Git)"
)

if st.button("Analyze Skills"):

    user_skills = [s.strip() for s in skills_input.split(",")]

    # Find missing skills
    missing = find_missing_skills(user_skills, role)

    # Load dataset
    df = pd.read_csv("dataset.csv")
    required_skills = df["skill"].tolist()

    # Calculate readiness
    score = readiness_score(user_skills, required_skills)

    st.subheader("Results")

    st.write(f"Readiness Score: {score:.2f}%")

    st.write("Missing Skills:")
    st.write(missing)
