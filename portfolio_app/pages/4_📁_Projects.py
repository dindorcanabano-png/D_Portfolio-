import streamlit as st

st.set_page_config(page_title="Projects | Dindo", page_icon="D", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #000000;
    color: #e8e6f0;
}

/* MAIN BACKGROUND */
.stApp {
    background-color: #000000 !important;
    color: #e8e6f0;
}

/* FIXED HEADER CSS (BROKEN IN YOUR ORIGINAL) */
header {
    background-color: #000000 !important;
}

[data-testid="stHeader"] {
    background-color: #000000 !important;
}

[data-testid="stHeader"]::before,
[data-testid="stHeader"]::after {
    display: none !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #0F5233 !important;
    border-right: none !important;
}

[data-testid="stSidebar"] * {
    color: #e8e6f0 !important;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.45rem 1.2rem;
    font-family: 'Syne', sans-serif;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(124,58,237,0.35);
}

/* ---------------- RESPONSIVE FIX ONLY ---------------- */
@media (max-width: 768px) {

    h1 {
        font-size: 2rem !important;
        text-align: center !important;
    }

    /* PROJECT CARDS STACK */
    div[style*="background:#13131f"] {
        width: 100% !important;
    }

    /* GRID → SINGLE COLUMN */
    [data-testid="column"] {
        width: 100% !important;
        flex: 100% !important;
    }

    /* TABS SPACING FIX */
    div[role="tablist"] {
        flex-wrap: wrap !important;
        gap: 0.5rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER (UNCHANGED) ----------------
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

# ---------------- TABS (UNCHANGED) ----------------
tab_all, tab_web, tab_sys, tab_data = st.tabs(["All", "Web Apps", "Systems", "Data"])

projects = [
    {
        "name": "Calculator (Calsai)",
        "category": "Systems",
        "description": "A mobile-style calculator built using Streamlit...",
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
        "description": "A web-based barangay management system...",
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
        "description": "This multipage Streamlit portfolio application...",
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
            background:#0a0a0f;
            border:1px solid #2a2a3e;
            border-radius:999px;
            padding:0.2rem 0.65rem;
            font-size:0.75rem;
            color:#00FF89;
            margin-right:0.35rem;
            margin-bottom:0.35rem;
            display:inline-block;
        ">{t}</span>"""
        for t in project["tech"]
    ])

    highlights_html = "".join([
        f"""<div style="display:flex; align-items:center; gap:0.6rem; padding:0.35rem 0;">
            <div style="width:5px; height:5px; border-radius:50%;
                        background:{project['color']};"></div>
            <span style="color:#b0afc8; font-size:0.82rem;">{h}</span>
        </div>"""
        for h in project["highlights"]
    ])

    return f"""
    <div style="
        background:#13131f;
        border:1px solid #2a2a3e;
        border-radius:18px;
        padding:1.75rem;
        height:100%;
    ">
        <p style="color:#e8e6f0; font-weight:700; font-size:1.05rem;">
            {project['name']}
        </p>

        <p style="color:#6b6b8a; font-size:0.85rem;">
            {project['description']}
        </p>

        <div style="margin-bottom:1rem;">{tech_badges}</div>

        <p style="color:#00FF89; font-weight:700;">Key Features</p>
        <div>{highlights_html}</div>
    </div>
    """

def display_projects(filtered):
    cols = st.columns(2)
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
        text-align:center;
        padding:3rem 1rem;
        background:#13131f;
        border:1px solid #2a2a3e;
        border-radius:16px;
    ">
        <p style="color:#6b6b8a;">
            Data science projects are in progress. Check back soon!
        </p>
    </div>
    """, unsafe_allow_html=True)
