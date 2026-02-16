import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.job_predictor import predict_job_role
from utils.ats_calculator import calculate_ats_score

st.title("AI Resume Analyzer & Job Matcher")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("Resume Text")
    st.write(text[:500])

    skills = extract_skills(text)
    st.subheader("Extracted Skills")
    st.write(skills)

    job = predict_job_role(skills)
    st.subheader("Suggested Job Role")
    st.write(job)

    score = calculate_ats_score(text)
    st.subheader("ATS Score")
    st.write(f"{score}/100")
