def calculate_ats_score(text):
    keywords = [
        "python", "sql", "machine learning",
        "data analysis", "communication",
        "project", "team", "ai"
    ]

    text = text.lower()
    score = sum(10 for k in keywords if k in text)

    return min(score, 100)
