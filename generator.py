import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def compile_pdf_resume(form_data):
    """Generates an ATS-compliant, print-ready document buffer."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    styles = getSampleStyleSheet()
    
    # Custom Structural Typography
    name_style = ParagraphStyle('Name', parent=styles['Heading1'], fontSize=24, leading=28, alignment=TA_CENTER, spaceAfter=4)
    contact_style = ParagraphStyle('Contact', parent=styles['Normal'], fontSize=10, leading=14, alignment=TA_CENTER, spaceAfter=15)
    section_heading = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=14, leading=18, spaceBefore=12, spaceAfter=6)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=11, leading=15, alignment=TA_LEFT, spaceAfter=6)
    
    # Header Mapping
    story.append(Paragraph(form_data.get('name', 'John Doe'), name_style))
    contact_info = f"{form_data.get('email', '')} | {form_data.get('phone', '')} | {form_data.get('location', '')}"
    story.append(Paragraph(contact_info, contact_style))
    
    # Structural Content Appending
    sections = [
        ("PROFESSIONAL SUMMARY", 'summary'),
        ("CORE SKILLS", 'skills'),
        ("PROFESSIONAL EXPERIENCE", 'experience'),
        ("EDUCATION", 'education')
    ]
    
    for label, key in sections:
        if form_data.get(key):
            story.append(Paragraph(label, section_heading))
            # Format single breaks cleanly
            text_block = form_data[key].replace('\n', '<br/>')
            story.append(Paragraph(text_block, body_style))
            story.append(Spacer(1, 8))
            
    doc.build(story)
    buffer.seek(0)
    return buffer