import streamlit as st
import plotly.graph_objects as go
from utils import extract_clean_pdf_text, analyze_resume_intelligence, generate_optimized_bullet_points
from generator import compile_pdf_resume

st.set_page_config(page_title="ResumeIQ AI Engine", page_icon="🎯", layout="wide")
st.title("🎯 ResumeIQ AI — Deep Career Intelligence Engine")
st.markdown("An advanced NLP analysis, parsing, optimization, and conversion platform.")

# Multi-Tier Control Layout Tab Architecture
tab_analyze, tab_create, tab_optimize = st.tabs([
    "🔍 Advanced Analysis & Job Matching", 
    "📝 AI Resume Builder & PDF Exporter", 
    "🤖 Bullet Point Optimizer"
])

# ==========================================
# TAB 1: ADVANCED ANALYSIS
# ==========================================
with tab_analyze:
    st.subheader("Deep Metric Matching Engine")
    col_a, col_b = st.columns(2)
    
    with col_a:
        jd_input = st.text_area("Target Job Description (JD)", height=250, placeholder="Paste requirements here...")
    with col_b:
        uploaded_file = st.file_uploader("Upload Active CV Profile (PDF)", type=["pdf"])
        
    if st.button("Run Intelligence Diagnostics"):
        if uploaded_file and jd_input.strip():
            with st.spinner("Extracting parameters and auditing alignment targets..."):
                try:
                    resume_text = extract_clean_pdf_text(uploaded_file)
                    report = analyze_resume_intelligence(resume_text, jd_input)
                    
                    st.success("Diagnostics Complete!")
                    st.markdown("---")
                    
                    # Row 1 metrics layout 
                    m1, m2, m3, m4, m5 = st.columns(5)
                    m1.metric("Overall Match", f"{report['scores']['overall']}%")
                    m2.metric("ATS Compatibility", f"{report['scores']['ats_compatibility']}%")
                    m3.metric("Content Quality", f"{report['scores']['content_quality']}%")
                    m4.metric("Skill Match", f"{report['scores']['skills_relevance']}%")
                    m5.metric("Experience Weight", f"{report['scores']['experience_weight']}%")
                    
                    st.markdown("---")
                    
                    # Row 2 layouts - Data Visualization Metrics
                    col_viz, col_txt = st.columns([4, 6])
                    
                    with col_viz:
                        st.subheader("🎯 Skill Gap vs Industry Benchmark")
                        fig = go.Figure()
                        fig.add_trace(go.Scatterpolar(
                            r=report['skill_matrix']['candidate_scores'],
                            theta=report['skill_matrix']['categories'],
                            fill='toself', name='Candidate'
                        ))
                        fig.add_trace(go.Scatterpolar(
                            r=report['skill_matrix']['industry_benchmarks'],
                            theta=report['skill_matrix']['categories'],
                            fill='toself', name='Market Benchmark'
                        ))
                        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True)
                        st.plotly_chart(fig, use_container_width=True)
                        
                    with col_txt:
                        st.subheader("👤 Extracted Profile Information")
                        st.json(report['parsing'])
                        
                        st.subheader("📈 Career Analytics & Growth Projections")
                        st.write(f"**Estimated Local Market Valuation (INR):** {report['career_growth']['salary_estimate_inr']}")
                        st.write("**Suggested Tracks:**", ", ".join(report['career_growth']['suggested_roles']))
                        st.write("**Target Certifications:**", ", ".join(report['career_growth']['recommended_certifications']))
                    
                    st.markdown("---")
                    col_crit1, col_crit2 = st.columns(2)
                    with col_crit1:
                        st.subheader("📋 Structural Strengths & Missing Elements")
                        st.write("**Core Strengths Identified:**")
                        for s in report['critique']['strengths']: st.markdown(f"- ✅ {s}")
                        st.write("**Flagged Missing Target Keywords:**")
                        for kw in report['critique']['missing_keywords']: st.markdown(f"- ❌ {kw}")
                    with col_crit2:
                        st.subheader("🕵️ Integrity Audit & Weaknesses")
                        st.write("**Observed Risk Indicators:**")
                        for w in report['critique']['fraud_risk_indicators']: st.markdown(f"- ⚠️ {w}")
                        
                    st.markdown("---")
                    st.subheader("📋 Contextual Interview Readiness Simulator")
                    for q in report['interview_prep']:
                        with st.expander(f"Type: {q['type']} | Expected Interview Scenario Question"):
                            st.write(f"**Question:** {q['question']}")
                            st.info(f"**Target Evaluation Key:** {q['target_answer']}")
                            
                except Exception as ex:
                    st.error(f"Engine Core Parsing Alert: {ex}")
        else:
            st.warning("Please provide both a matching JD and a target PDF resume.")

# ==========================================
# TAB 2: AI RESUME BUILDER
# ==========================================

# ==========================================
# TAB 2: AI RESUME BUILDER
# ==========================================
with tab_create:
    st.subheader("Compile Print-Ready ATS Document")
    
    # 1. Initialize a session state variable to store the compiled PDF across browser reruns
    if "compiled_pdf" not in st.session_state:
        st.session_state.compiled_pdf = None

    # 2. The Form Container (Only contains text inputs and a submission button)
    with st.form("builder_form"):
        cb_name = st.text_input("Full Name", value="Alex Martin")
        c1, c2, c3 = st.columns(3)
        cb_email = c1.text_input("Email ID", value="alex.martin@email.com")
        cb_phone = c2.text_input("Phone Number", value="+91 98765 43210")
        cb_loc = c3.text_input("Location", value="Bangalore, India")
        
        cb_summary = st.text_area("Professional Summary", value="Data Science & AI Graduate specializing in engineering custom analytics systems.")
        cb_skills = st.text_area("Skills (Comma Separated)", value="Python, SQL, Power BI, Pandas, NumPy, Scikit-Learn")
        cb_exp = st.text_area("Professional Experience / Project Work Blocks", value="Data Project Engineer\n- Developed predictive systems yielding 15% latency drop.\n- Built Power BI dashboards.")
        cb_edu = st.text_area("Education Details", value="B.Tech in Computer Science (Specialization in AI), 2025")
        
        # Form submit button (Safe!)
        generate_pdf = st.form_submit_button("Compile Professional Layout")
        
        if generate_pdf:
            payload = {
                "name": cb_name, "email": cb_email, "phone": cb_phone, "location": cb_loc,
                "summary": cb_summary, "skills": cb_skills, "experience": cb_exp, "education": cb_edu
            }
            # Save the compiled binary bytes to session state memory
            st.session_state.compiled_pdf = compile_pdf_resume(payload)
            st.success("ATS Resume Compiled Successfully! Download your file below.")

    # 3. Render the download button SAFELY outside the form layout boundary
    if st.session_state.compiled_pdf is not None:
        st.markdown("### 📥 Your Generated Document is Ready")
        st.download_button(
            label="📥 Download Structured Document PDF", 
            data=st.session_state.compiled_pdf, 
            file_name="ResumeIQ_Optimized.pdf", 
            mime="application/pdf"
        )
# ==========================================
# TAB 3: BULLET POINT OPTIMIZER
# ==========================================
with tab_optimize:
    st.subheader("Improve Action Verbs & Quantify Achievements")
    raw_text_block = st.text_area("Paste static description phrases here:", height=150, placeholder="e.g., I was responsible for looking after sql databases and doing testing.")
    if st.button("Optimize Phrases"):
        if raw_text_block.strip():
            with st.spinner("Refactoring expressions..."):
                optimized_result = generate_optimized_bullet_points(raw_text_block)
                st.subheader("✨ Optimized Result (Copy & Paste to Form Builder)")
                st.markdown(optimized_result)
        else:
            st.warning("Please enter some text to refine.")