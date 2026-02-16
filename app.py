import streamlit as st
import fitz  # PyMuPDF

# Import your utils
from utils.skill_extractor import extract_skills
from utils.job_matcher import match_resume_job

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Resume Analyzer — Pro Version")
st.write("Upload your resume and analyze skills, ATS score, and job match.")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("⚙️ Settings")
show_text = st.sidebar.checkbox("Show Resume Text")

# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

# Job description input
job_desc = st.text_area("Paste Job Description (Optional)")

# -------------------------------
# FUNCTION → EXTRACT TEXT FROM PDF
# -------------------------------
def extract_text(pdf_file):
    text = ""
    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text


# -------------------------------
# FUNCTION → ATS SCORE
# -------------------------------
def calculate_ats(resume_text, job_desc):
    if not job_desc:
        return 50  # default score

    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())

    if len(job_words) == 0:
        return 0

    score = len(resume_words.intersection(job_words)) / len(job_words) * 100
    return round(score, 2)


# -------------------------------
# MAIN PROCESS
# -------------------------------
if uploaded_file:

    if st.button("Analyze Resume"):

        # Extract resume text
        resume_text = extract_text(uploaded_file)

        if not resume_text.strip():
            st.error("Could not extract text from PDF.")
            st.stop()

        st.success("Resume uploaded successfully!")

        col1, col2 = st.columns(2)

        # -------------------------------
        # SHOW RESUME TEXT
        # -------------------------------
        if show_text:
            with st.expander("Resume Text"):
                st.write(resume_text)

        # -------------------------------
        # SKILLS EXTRACTION
        # -------------------------------
        skills = extract_skills(resume_text)

        with col1:
            st.subheader("🧠 Extracted Skills")

            if skills:
                for skill in skills:
                    st.write("✅", skill)
            else:
                st.write("No skills detected")

        # -------------------------------
        # JOB MATCH SCORE
        # -------------------------------
        with col2:
            st.subheader("🎯 Job Match Score")

            if job_desc:
                match_score = match_resume_job(resume_text, job_desc)
                st.progress(int(match_score))
                st.write(f"{match_score}% match")
            else:
                st.info("Enter job description to see match score")

        # -------------------------------
        # ATS SCORE
        # -------------------------------
        ats_score = calculate_ats(resume_text, job_desc)

        st.subheader("📊 ATS Score")
        st.progress(int(ats_score))
        st.write(f"{ats_score}/100")

        # -------------------------------
        # SUGGESTED ROLE
        # -------------------------------
        st.subheader("💼 Suggested Job Role")

        if "python" in resume_text.lower():
            st.write("Software Developer / Data Analyst")
        elif "java" in resume_text.lower():
            st.write("Java Developer")
        elif "machine learning" in resume_text.lower():
            st.write("Machine Learning Engineer")
        else:
            st.write("General IT Role")

