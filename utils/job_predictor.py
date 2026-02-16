def predict_job_role(skills):
    if "Python" in skills:
        return "Python Developer"
    elif "Machine Learning" in skills:
        return "ML Engineer"
    elif "SQL" in skills:
        return "Database Engineer"
    else:
        return "General IT Role"
