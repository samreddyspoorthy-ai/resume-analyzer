import streamlit as st
import matplotlib.pyplot as plt

from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.job_matcher import match_resume_job
from utils.feedback_generator import skill_gap_analysis, generate_resume_feedback
from utils.report_generator import generate_pdf_report

st.title("🚀 AI Resume Analyzer — Pro Version")

uploaded_file = st.file_uploader("Upload Resume PDF", type="pdf")

job_desc = st.text_area("Paste Job Description")

required_skills = [
    "Python", "SQL", "Machine Learning",
    "Data Analysis", "Communication"
]

if uploaded_file and job_desc:

    text = extract_text_from_pdf(uploaded_file)
    found_skills = extract_skills(text)

    score = match_resume_job(text, job_desc)
    missing = skill_gap_analysis(found_skills, required_skills)
    feedback = generate_resume_feedback(score, missing)

    st.subheader("📊 Job Match Score")
    st.write(f"{score}%")

    st.subheader("🧠 Detected Skills")
    st.write(found_skills)

    st.subheader("❌ Missing Skills")
    st.write(missing)

    st.subheader("💡 AI Suggestions")
    for f in feedback:
        st.write("•", f)

    # Chart
    st.subheader("📈 Skill Score Chart")
    fig, ax = plt.subplots()
    ax.bar(["Match Score"], [score])
    st.pyplot(fig)

    # PDF Download
    if st.button("Download Report"):
        pdf_file = generate_pdf_report(score, found_skills, feedback)

        with open(pdf_file, "rb") as f:
            st.download_button("Download PDF", f, file_name=pdf_file)
