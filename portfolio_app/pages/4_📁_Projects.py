 import streamlit as st

st.set_page_config(page_title="Projects | Dindo", page_icon="D", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0a0f; color: #e8e6f0;
}
/* MAIN BACKGROUND (BLACK FIX) */
.stApp {
    background-color: #000000 !important;
    color: #e8e6f0;
/* ✅ FIX WHITE HEADER */
header {
    background-color: #000000 !important;
}

[data-testid="stHeader"] {
    background-color: #000000 !important;
}

/* remove header lines/shadow */
[data-testid="stHeader"]::before,
[data-testid="stHeader"]::after {
    display: none !important;
}
            
/* =========================
   SIDEBAR (UPDATED COLOR)
   ========================= */
[data-testid="stSidebar"] {
    background: #0F5233 !important;
    border-right: none !important;
}

/* Sidebar text fix */
[data-testid="stSidebar"] * {
    color: #e8e6f0 !important;
}

/* TEXT */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5); color: white;
    border: none; border-radius: 8px; padding: 0.45rem 1.2rem;
    font-family: 'Syne', sans-serif; font-weight: 600;
    box-shadow: 0 4px 15px rgba(124,58,237,0.35);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family:'Syne',sans-serif; font-size:0.82rem; font-weight:600;
    letter-spacing:0.18em; color:#00FF89; text-transform:uppercase;
    padding-top:1.5rem; margin-bottom:0.5rem;
">What I've Built</p>
<h1 style="
    font-family:'Syne',sans-serif; font-size:2.6rem; font-weight:800;
    background: linear-gradient(135deg, #e8e6f0 40%, #a78bfa);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    margin-bottom:0.25rem;
">My Projects</h1>
<hr style="border-color:#00FF89; margin-bottom:2rem;">
""", unsafe_allow_html=True)

tab_all, tab_web, tab_sys, tab_data = st.tabs(["All", "Web Apps", "Systems", "Data"])

projects = [
    {
        "name": "Calculator (Calsai)",
        "category": "Systems",
        "description": "A mobile-style calculator built using Streamlit, featuring a clean responsive UI and voice input capability for hands-free calculations.",
        "tech": ["Python", "Streamlit", "SpeechRecognition", "Base64", "gtts"],
        "status": "Completed",
        "color": "#143219",
        "highlights": [
            "Mobile-style calculator interface",
            "Basic arithmetic operations",
            "Voice input for calculations",
            "Clean and responsive UI design",
        ],
    },
    {
        "name": "Barangay Management System",
        "category": "Systems",
        "description": "A web-based barangay management system built using PHP and XAMPP, designed to handle resident records, clearances, and administrative processes efficiently.",
        "tech": ["PHP", "MySQL", "XAMPP", "HTML/CSS"],
        "status": "Completed",
        "color": "#569D64",
        "highlights": [
            "Resident record management",
            "Barangay clearance processing",
            "Admin dashboard system",
            "Database integration using MySQL",
        ],
    },
    {
        "name": "Portfolio Web App",
        "category": "Web Apps",
        "description": "This multipage Streamlit portfolio application, designed and built from scratch to showcase my work, skills, and journey as a developer.",
        "tech": ["Python", "Streamlit", "CSS", "GitHub"],
        "status": "Live",
        "color": "#56935a",
        "highlights": [
            "Custom CSS styling",
            "Multi-page navigation",
            "Deployed on Streamlit Cloud",
            "Responsive layout",
        ],
    },
]

def render_project_card(project):
    status_color = "#22c55e" if project["status"] == "Live" else "#ffffff"
    tech_badges = "".join([
        f"""<span style="
            background:#0a0a0f; border:1px solid #2a2a3e; border-radius:999px;
            padding:0.2rem 0.65rem; font-size:0.75rem; color:#00FF89;
            margin-right:0.35rem; margin-bottom:0.35rem; display:inline-block;
        ">{t}</span>"""
        for t in project["tech"]
    ])
    highlights_html = "".join([
        f"""<div style="
                display:flex; align-items:center; gap:0.6rem;
                padding:0.35rem 0; border-bottom:1px solid #1a1a2a;
            ">
            <div style="
                width:5px; height:5px; border-radius:50%;
                background:{project['color']}; flex-shrink:0;
            "></div>
            <span style="color:#b0afc8; font-size:0.82rem;">{h}</span>
        </div>"""
        for h in project["highlights"]
    ])
    return f"""
    <div style="
        background:#13131f; border:1px solid #2a2a3e; border-radius:18px;
        padding:1.75rem; height:100%; position:relative; overflow:hidden;
        transition:border-color 0.2s;
    ">
        <div style="
            position:absolute; top:0; left:0; right:0; height:3px;
            background: linear-gradient(90deg, {project['color']}88, {project['color']});
        "></div>
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.9rem;">
            <div style="
                background:{project['color']}22; border:1px solid {project['color']}44;
                border-radius:8px; padding:0.5rem 0.75rem;
            ">
                <span style="font-family:'Syne',sans-serif; font-weight:800;
                             color:{project['color']}; font-size:0.85rem;">
                    {project['name'][0]}{project['name'].split()[1][0] if len(project['name'].split()) > 1 else ''}
                </span>
            </div>
            <span style="
                background:{status_color}22; border:1px solid {status_color}44;
                border-radius:999px; padding:0.2rem 0.7rem;
                font-size:0.75rem; color:{status_color}; font-weight:600;
            ">{project['status']}</span>
        </div>
        <p style="
            font-family:'Syne',sans-serif; font-weight:700;
            color:#e8e6f0; font-size:1.05rem; margin-bottom:0.6rem;
        ">{project['name']}</p>
        <p style="color:#6b6b8a; font-size:0.85rem; line-height:1.65; margin-bottom:1rem;">
            {project['description']}
        </p>
        <div style="margin-bottom:1rem;">{tech_badges}</div>
        <p style="font-family:'Syne',sans-serif; font-weight:700;
                  color:#00FF89; font-size:0.82rem; margin-bottom:0.5rem;">
            Key Features
        </p>
        <div>{highlights_html}</div>
    </div>
    """

def display_projects(filtered):
    if not filtered:
        st.info("No projects in this category yet.")
        return
    cols = st.columns(2, gap="medium")
    for i, proj in enumerate(filtered):
        with cols[i % 2]:
            st.markdown(render_project_card(proj), unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

with tab_all:
    display_projects(projects)

with tab_web:
    display_projects([p for p in projects if p["category"] == "Web Apps"])

with tab_sys:
    display_projects([p for p in projects if p["category"] == "Systems"])

with tab_data:
    st.markdown("""
    <div style="
        text-align:center; padding:3rem 1rem;
        background:#13131f; border:1px solid #2a2a3e;
        border-radius:16px; margin-top:1rem;
    ">
        <p style="color:#6b6b8a; font-size:0.95rem;">
            Data science projects are in progress. Check back soon!
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="
    background: linear-gradient(135deg, #13131f, #1a1a2e);
    border:1px solid #2a2a3e; border-radius:16px; padding:2rem;
    text-align:center;
">
    <p style="font-family:'Syne',sans-serif; font-weight:800;
              font-size:1.3rem; color:#00FF89; margin-bottom:0.5rem;">
        Interested in collaborating?
    </p>
    <p style="color:#6b6b8a; font-size:0.88rem; margin-bottom:1.25rem;">
        I'm always open to exciting new projects and opportunities.
    </p>
</div>
""", unsafe_allow_html=True)
