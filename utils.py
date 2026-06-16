import os
import json
import pdfplumber
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_clean_pdf_text(uploaded_file):
    """Extracts raw string layouts from structured PDF files."""
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def analyze_resume_intelligence(resume_text, job_description):
    """Sends prompt configuration to model, enforcing strict structural JSON parsing."""
    model = genai.GenerativeModel('gemini-3.5-flash')
    
    prompt = f"""
    You are an advanced AI Career Coach and ATS Engine named ResumeIQ.
    Analyze the provided Resume Text against the Job Description.
    You must output a single valid JSON object exactly matching the scheme below. 
    Do not add markdown formatting, headers, or surrounding backticks outside the JSON.

    Required JSON Blueprint Structure:
    {{
      "scores": {{
        "overall": 85,
        "ats_compatibility": 90,
        "content_quality": 80,
        "skills_relevance": 85,
        "experience_weight": 75
      }},
      "parsing": {{
        "name": "Candidate Name or Unknown",
        "email": "Email or Unknown",
        "phone": "Phone or Unknown",
        "detected_level": "Junior/Mid/Senior/Fresher"
      }},
      "skill_matrix": {{
        "categories": ["Languages", "Databases", "Cloud", "Tools"],
        "candidate_scores": [80, 70, 40, 90],
        "industry_benchmarks": [90, 85, 75, 80]
      }},
      "critique": {{
        "strengths": ["List item 1", "List item 2"],
        "weaknesses": ["List item 1"],
        "missing_keywords": ["Keyword1", "Keyword2"],
        "fraud_risk_indicators": ["None identified" or flag descriptions]
      }},
      "career_growth": {{
        "salary_estimate_inr": "6,00,000 - 9,00,000",
        "recommended_certifications": ["Cert 1", "Cert 2"],
        "suggested_roles": ["Role 1", "Role 2"]
      }},
      "interview_prep": [
        {{"type": "Technical", "question": "Question text?", "target_answer": "Key talking points to address"}},
        {{"type": "Behavioral", "question": "Question text?", "target_answer": "Key talking points to address"}}
      ]
    }}

    Resume Text:
    {resume_text}

    Job Description:
    {job_description}
    """
    
    response = model.generate_content(prompt)
    clean_text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(clean_text)

def generate_optimized_bullet_points(raw_experience_text):
    """Rewrites weak strings into impactful professional achievements."""
    model = genai.GenerativeModel('gemini-3.5-flash')
    prompt = f"""
    Rewrite these resume bullet points to use powerful action verbs, optimize for ATS layout, and quantify achievements:
    {raw_experience_text}
    Provide the response as an explicit bulleted list.
    """
    response = model.generate_content(prompt)
    return response.text