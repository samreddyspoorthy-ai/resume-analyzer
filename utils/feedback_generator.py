def skill_gap_analysis(found_skills, required_skills):
    missing = []

    for skill in required_skills:
        if skill.lower() not in [s.lower() for s in found_skills]:
            missing.append(skill)

    return missing


def generate_resume_feedback(score, missing_skills):
    feedback = []

    if score > 80:
        feedback.append("Excellent match for job role.")
    elif score > 60:
        feedback.append("Good profile but needs improvements.")
    else:
        feedback.append("Low match. Resume needs major improvement.")

    if missing_skills:
        feedback.append("Add these skills: " + ", ".join(missing_skills))

    feedback.append("Use action verbs like Developed, Built, Created.")
    feedback.append("Add measurable achievements.")

    return feedback
