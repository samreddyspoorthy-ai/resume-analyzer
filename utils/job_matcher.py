def match_resume_job(resume_text, job_desc):

    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())

    match = resume_words.intersection(job_words)

    if len(job_words) == 0:
        return 0

    score = len(match)/len(job_words)*100
    return round(score,2)
