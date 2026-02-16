import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.job_predictor import predict_job_role
from utils.ats_calculator import calculate_ats_score

# Page settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 AI Resume Analyzer & Job Matcher")
st.markdown("Upload your resume → Get job suggestions, ATS score, and skill analysis")

st.divider()

# Upload section
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

if uploaded_file:

    with st.spinner("Analyzing Resume..."):
        text = extract_text_from_pdf(uploaded_file)
        skills = extract_skills(text)
        job_role = predict_job_role(skills)
        ats_score = calculate_ats_score(text)

    st.success("Analysis Complete ✅")

    col1, col2 = st.columns(2)

    # Resume Preview
    with col1:
        st.subheader("📄 Resume Preview")
        st.text_area("", text, height=300)

    # Skills
    with col2:
        st.subheader("🧠 Extracted Skills")

        if skills:
            skill_html = ""
            for skill in skills:
                skill_html += f"""
                <span style="
                background:#1f77b4;
                padding:8px;
                border-radius:8px;
                margin:5px;
                display:inline-block;
                color:white;">
                {skill}
                </span>
                """
            st.markdown(skill_html, unsafe_allow_html=True)
        else:
            st.warning("No skills detected")

    st.divider()

    # Results Section
    col3, col4 = st.columns(2)

    # Job Role
    with col3:
        st.subheader("💼 Suggested Job Role")
        st.success(job_role)

    # ATS Score
    with col4:
        st.subheader("📊 ATS Score")
        st.progress(ats_score / 100)
        st.metric("Score", f"{ats_score}/100")

        if ats_score < 50:
            st.error("Needs improvement")
        elif ats_score < 75:
            st.warning("Good but can improve")
        else:
            st.success("Excellent resume")

    st.divider()

    # Skill Gap Suggestions
    st.subheader("📚 Recommended Learning")

    missing_skills = ["Machine Learning", "Cloud", "System Design"]

    for skill in missing_skills:
        if skill not in skills:
            st.write("✅ Learn:", skill)
