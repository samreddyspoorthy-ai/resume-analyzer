import spacy

nlp = spacy.load("en_core_web_sm")

skills_db = [
    "python","sql","machine learning","ai",
    "deep learning","java","html","css","javascript"
]

def extract_skills(text):
    text = text.lower()
    doc = nlp(text)

    found = []
    for token in doc:
        if token.text in skills_db:
            found.append(token.text)

    return list(set(found))
