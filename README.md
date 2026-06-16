# 🎯 ResumeIQ AI

> An AI-powered Resume Analyzer, ATS Optimizer, Career Intelligence Platform, and Interview Preparation Assistant.

ResumeIQ AI helps job seekers create stronger resumes, improve ATS compatibility, identify skill gaps, prepare for interviews, and generate professional resumes using Generative AI.

---

## 🚀 Features

### 📄 Resume Analysis

* Upload PDF resumes
* Extract resume information automatically
* Analyze resume structure and content quality
* Identify missing sections and weaknesses
* Generate actionable improvement suggestions

### 🎯 ATS Optimization

* ATS compatibility scoring
* Keyword analysis and optimization
* Resume formatting evaluation
* Section structure recommendations
* Job Description matching

### 📊 Resume Scoring Engine

* Overall Resume Score
* ATS Score
* Skills Relevance Score
* Experience Score
* Education Score
* Content Quality Score

### 🔍 Skill Gap Analysis

* Extract technical and soft skills
* Compare candidate skills against job requirements
* Identify missing skills
* Recommend learning paths and certifications
* Interactive skill visualization dashboard

### 🤖 AI Resume Enhancement

* Rewrite weak bullet points
* Improve professional summaries
* Generate achievement-oriented content
* Optimize language using action verbs
* Quantify accomplishments automatically

### 📝 Resume Generator

* Create ATS-friendly resumes
* Generate professional PDF resumes
* Single-page optimized layouts
* Export ready-to-share documents

### 🎤 Interview Preparation

* Generate technical interview questions
* Generate HR interview questions
* Behavioral interview preparation
* Skill-based mock interview questions
* Personalized interview readiness reports

### 🛡️ Resume Integrity Checks

* Detect buzzword stuffing
* Identify inconsistent experience timelines
* Flag suspicious content patterns
* Improve credibility and authenticity

---

## 🏗️ System Architecture

```text
Resume Upload (PDF)
        │
        ▼
 Resume Parser
(pdfplumber)
        │
        ▼
 Information Extraction
        │
        ▼
 Gemini AI Analysis Engine
        │
 ┌──────┼────────┬──────────┐
 ▼      ▼        ▼          ▼
ATS   Skill   Resume   Interview
Score  Gap    Improve   Questions
      Analysis
 └──────┼────────┴──────────┘
        ▼
 Interactive Dashboard
        │
        ▼
 PDF Resume Generator
```

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI & NLP

* Google Gemini API

### Document Processing

* pdfplumber

### Data Analysis

* Pandas

### Visualization

* Plotly

### PDF Generation

* ReportLab

### Environment Management

* Python
* python-dotenv

---

## 📁 Project Structure

```text
resumeiq-ai/
│
├── app.py
├── utils.py
├── generator.py
├── requirements.txt
├── .env
├── .gitignore
│
└── assets/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/resumeiq-ai.git

cd resumeiq-ai
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your API key from Google AI Studio.

### 5. Run the Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 📦 Requirements

```text
streamlit
google-generativeai
pdfplumber
reportlab
plotly
pandas
python-dotenv
```

---

## 🔒 Security

* API keys are stored securely in `.env`
* `.env` is excluded using `.gitignore`
* No credentials are hardcoded
* Local cache files are ignored

---

## 🎯 Use Cases

* Students building their first resume
* Internship applicants
* Job seekers optimizing ATS scores
* Career coaches and mentors
* Placement cell assistance
* Hackathon and portfolio projects

---

## 🚀 Future Enhancements

* LinkedIn Profile Analyzer
* Resume Ranking System
* Cover Letter Generator
* Job Recommendation Engine
* Salary Prediction Module
* Multi-language Resume Support
* Resume vs Job Match Percentage
* Voice-based Interview Simulator

---

## 👨‍💻 Author

**Dyuti Asok B**

* GitHub: https://github.com/dyuticode
* LinkedIn: https://www.linkedin.com/in/dyuti-asok-5b5b00366/

---

⭐ If you found this project useful, consider giving it a star on GitHub.
