from agents.skill_gap_agent import analyze_skill_gap
from agents.roadmap_agent import generate_roadmap
from agents.resume_agent import analyze_resume
from agents.ats_score_agent import analyze_ats_score
from agents.career_readiness_agent import analyze_career_readiness
from agents.project_recommendation_agent import recommend_projects
from agents.interview_agent import generate_interview_questions
from agents.job_matching_agent import match_jobs
from agents.course_recommendation_agent import recommend_courses


def generate_career_plan(skills, goal, resume_text):

    skill_gap = analyze_skill_gap(skills, goal)

    

    roadmap = generate_roadmap(skills, goal)

    resume = analyze_resume(resume_text, goal)

    ats_score = analyze_ats_score(
    resume_text,
    goal
)

    readiness = analyze_career_readiness(
    skills,
    goal
)
    
    projects = recommend_projects(
    skills,
    goal
)
    
    interview = generate_interview_questions(skills, goal)

    job_match = match_jobs(skills, goal)

    courses = recommend_courses(
    skills,
    goal
)

    

    return {
        "skill_gap": skill_gap,
        "roadmap": roadmap,
        "resume": resume,
        "ats_score": ats_score,
        "readiness": readiness,
        "projects": projects,
        "interview": interview,
        "job_match": job_match,
        "courses": courses
    }