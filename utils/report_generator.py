from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(score, skills, feedback):
    file_name = "resume_report.pdf"
    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Resume Analysis Report", styles["Title"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Job Match Score: {score}%", styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Detected Skills:", styles["Heading2"]))
    elements.append(Paragraph(", ".join(skills), styles["Normal"]))

    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Feedback:", styles["Heading2"]))

    for f in feedback:
        elements.append(Paragraph(f, styles["Normal"]))

    doc.build(elements)

    return file_name
