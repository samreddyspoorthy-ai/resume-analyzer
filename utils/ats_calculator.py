def calculate_ats_score(text):
    keywords = ["experience", "project", "skills", "education"]
    score = sum(1 for k in keywords if k in text.lower())
    return score * 25
