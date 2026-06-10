import streamlit as st
from utils.pdf_reader import extract_pdf_text

from agents.skill_gap_agent import analyze_skill_gap
from agents.roadmap_agent import generate_roadmap
from agents.resume_agent import analyze_resume
from agents.ats_score_agent import analyze_ats_score
from agents.career_readiness_agent import analyze_career_readiness
from agents.project_recommendation_agent import recommend_projects
from agents.interview_agent import generate_interview_questions
from agents.job_matching_agent import match_jobs
from agents.job_market_agent import analyze_job_market
from agents.course_recommendation_agent import recommend_courses
from agents.linkedin_analyzer_agent import analyze_linkedin_profile
from agents.career_chatbot_agent import career_chatbot

# Page Config
st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🚀 AI Career Copilot")

    st.markdown("""
    ### Features

    ✅ Skill Gap Analysis

    ✅ Learning Roadmap

    ✅ Resume Suggestions
                
    ✅ ATS Score Analysis 

    ✅ Career Readiness Analysis 

    ✅ Project Recommendations        

    ✅ Interview Preparation
                
    ✅ Job Matching 
                
    ✅ Job Market Intelligence  

    ✅ Course Recommendations 

    ✅ LinkedIn Profile Analysis

         
    """)

# Main Title
st.title("🚀 AI Career Copilot")

st.caption("Multi-Agent Career Guidance System using AI")

st.markdown("""
Generate a complete AI-powered career plan based on your
skills, goals, and resume.
""")

# Input Section
col1, col2 = st.columns(2)

with col1:
    skills = st.text_area("Current Skills")

with col2:
    goal = st.text_input("Career Goal")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

resume_text = ""

if uploaded_file:
    resume_text = extract_pdf_text(uploaded_file)

    st.success("✅ Resume Uploaded Successfully")

# Skill Gap
st.subheader("📊 Skill Gap Analysis")

if st.button("Generate Skill Gap"):
    if not skills or not goal:
        st.warning("Please enter Skills and Career Goal")
    else:
        with st.spinner("Analyzing Skill Gap..."):
            result = analyze_skill_gap(skills, goal)

    st.markdown(result)

# Roadmap
st.subheader("🗺 Learning Roadmap")

if st.button("Generate Roadmap"):
    if not skills or not goal:
        st.warning("Please enter Skills and Career Goal")
    else:
        with st.spinner("Generating Roadmap..."):
            result = generate_roadmap(skills, goal)

    st.markdown(result)

# Resume
st.subheader("📄 Resume Suggestions")

if st.button("Analyze Resume"):
    if not resume_text or not goal:
        st.warning("Please enter Skills and Career Goal")
    else:
        with st.spinner("Analyzing Resume..."):
            result = analyze_resume(resume_text,goal)

    st.markdown(result)

# ATS Score
if st.button("Calculate ATS Score"):

    if not resume_text or not goal:
        st.warning(
            "Please upload resume and enter Career Goal"
        )

    else:
        with st.spinner("Calculating ATS Score..."):
            result = analyze_ats_score(
                resume_text,
                goal
            )

        st.write(result)

# Career Readiness
st.subheader("🎯 Career Readiness")

if st.button("Analyze Readiness"):
    if not skills or not goal:
        st.warning("Please enter Skills and Career Goal")
    else:
        with st.spinner("Analyzing Readiness..."):
            result = analyze_career_readiness(skills, goal)

    st.write(result)

# Project Recommendation
st.subheader("🚀 Project Recommendations")

if st.button("Generate Project Recommendation"):
    if not skills or not goal:
        st.warning("Please enter Skills and Career Goal")
    else:
        with st.spinner("project recommendation..."):
            result = recommend_projects(skills, goal)

    st.write(result)

# Interview Questions
st.subheader("🎤 Interview Questions")

if st.button("Generate Questions"):
    if not skills or not goal:
        st.warning("Please enter Skills and Career Goal")
    else:
        with st.spinner("Generating Questions..."):
            result = generate_interview_questions(skills, goal)

    st.markdown(result)

# Job Matching
st.subheader("💼 Job Matching")

if st.button("Match Jobs"):
    if not skills or not goal:
        st.warning("Please enter Skills and Career Goal")
    else:
        with st.spinner("Finding Jobs..."):
            result = match_jobs(skills, goal)

    st.markdown(result)

# job market
st.subheader("📊 Job Market Intelligence")

if st.button("Analyze Job Market"):

    if not goal:
        st.warning(
            "Please enter Career Goal"
        )

    else:

        with st.spinner(
            "Analyzing Job Market..."
        ):

            result = analyze_job_market(goal)

        st.write(result)


# Course Recommendations
st.subheader("📚 Course Recommendations")

if st.button("Recommend Courses"):

    if not skills or not goal:
        st.warning(
            "Please enter Skills and Career Goal"
        )

    else:
        with st.spinner(
            "Finding Learning Resources..."
        ):

            result = recommend_courses(
                skills,
                goal
            )

        st.write(result)

# Linkedin analyzer
st.subheader("🔗 LinkedIn Profile Analyzer")

linkedin_text = st.text_area(
    "Paste LinkedIn Summary",
    height=200
)

if st.button("Analyze LinkedIn Profile"):

    if not linkedin_text:
        st.warning(
            "Please paste LinkedIn profile summary"
        )

    else:

        with st.spinner(
            "Analyzing LinkedIn Profile..."
        ):

            result = analyze_linkedin_profile(
                linkedin_text
            )

        st.write(result)


# AI chatbot
st.subheader("🤖 AI Career Coach chatbot")

user_question = st.text_input(
    "Ask a Career Question"
)

if st.button("Ask Career Coach"):

    if not user_question:

        st.warning(
            "Please enter a question"
        )

    else:

        with st.spinner(
            "Thinking..."
        ):

            response = career_chatbot(
                user_question
            )

        st.write(response)

st.markdown("---")
