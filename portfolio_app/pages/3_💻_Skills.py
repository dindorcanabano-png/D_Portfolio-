import streamlit as st

st.set_page_config(page_title="Skills | Dindo", page_icon="D", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* MAIN BACKGROUND */
.stApp {
    background-color: #000000 !important;
    color:#e8e6f0;
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

/* HEADINGS */
h1, h2, h3 {
    font-family: 'Syne', sans-serif;
    letter-spacing: -0.02em;
}

/* HR */
hr {
    border-color: #1e1e2e;
}

/* PROGRESS BAR */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #7c3aed, #60a5fa);
    border-radius: 999px;
}

/* HIDE UI */
#MainMenu, footer, header {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family:'Syne',sans-serif;
    font-size:0.82rem;
    font-weight:600;
    letter-spacing:0.18em;
    color:#00FF89;
    text-transform:uppercase;
    padding-top:1.5rem;
    margin-bottom:0.5rem;
">Technical Profile</p>

<h1 style="
    font-family:'Syne',sans-serif;
    font-size:2.6rem;
    font-weight:800;
    background: linear-gradient(135deg, #e8e6f0 40%, #a78bfa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:0.25rem;
">Skills & Expertise</h1>

<hr style="border-color:#00FF89; margin-bottom:2rem;">
""", unsafe_allow_html=True)

col_prog, col_tools = st.columns([1.4, 1], gap="large")

with col_prog:
    categories = {
        "Programming Languages": [
            ("Python", 82, "#60a5fa"),
            ("HTML & CSS", 90, "#34d399"),
            ("C", 68, "#f472b6"),
        ],
        "Frameworks & Libraries": [
            ("Streamlit", 85, "#7c3aed"),
            ("Bootstrap", 72, "#818cf8"),
        ],
        "Design": [
            ("Canva / UI Design", 88, "#f472b6"),
            ("Figma (Basic)", 45, "#fb923c"),
            ("Responsive Layouts", 80, "#34d399"),
        ],
    }

    for category, skills in categories.items():
        st.markdown(f"""
        <p style="
            font-family:'Syne',sans-serif;
            font-weight:700;
            color:#00FF89;
            font-size:1rem;
            margin:1.5rem 0 1rem;
        ">{category}</p>
        """, unsafe_allow_html=True)

        for skill_name, level, color in skills:
            st.markdown(f"""
            <div style="margin-bottom:1.1rem;">
                <div style="display:flex; justify-content:space-between; margin-bottom:0.35rem;">
                    <span style="font-size:0.88rem; color:#b0afc8;">
                        {skill_name}
                    </span>
                    <span style="font-size:0.82rem; color:{color}; font-weight:600;">
                        {level}%
                    </span>
                </div>
                <div style="background:#1a1a2e; border-radius:999px; height:7px;">
                    <div style="
                        width:{level}%;
                        height:100%;
                        border-radius:999px;
                        background:linear-gradient(90deg, {color}88, {color});
                    "></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

with col_tools:
    st.markdown("""
    <p style="
        font-family:'Syne',sans-serif;
        font-weight:700;
        color:#00FF89;
        font-size:1rem;
        margin:0 0 1rem;
    ">Tools I Use</p>
    """, unsafe_allow_html=True)

    tools = [
        ("GitHub", "Version control and collaboration", "#e8e6f0"),
        ("VS Code", "Primary code editor", "#60a5fa"),
        ("Streamlit", "Python web apps", "#7c3aed"),
        ("XAMPP", "Local PHP/MySQL server", "#f59e0b"),
        ("Canva", "Graphic design and UI mockups", "#f472b6"),
    ]

    for tool, desc, color in tools:
        st.markdown(f"""
        <div style="
            background:#13131f;
            border:1px solid #2a2a3e;
            border-radius:12px;
            padding:0.9rem 1.1rem;
            margin-bottom:0.65rem;
            display:flex;
            align-items:center;
            gap:0.85rem;
        ">
            <div style="
                width:36px;
                height:36px;
                border-radius:8px;
                background:linear-gradient(135deg,{color}22,{color}44);
                border:1px solid {color}44;
                display:flex;
                align-items:center;
                justify-content:center;
                font-weight:800;
                color:{color};
            ">
                {tool[0]}
            </div>
            <div>
                <p style="margin:0; color:#e8e6f0; font-weight:600;">
                    {tool}
                </p>
                <p style="margin:0; color:#6b6b8a; font-size:0.75rem;">
                    {desc}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family:'Syne',sans-serif;
    font-weight:700;
    color:#e8e6f0;
">
Soft Skills
</p>
""", unsafe_allow_html=True)

soft_cols = st.columns(4)

soft_skills = [
    ("Problem Solving", "Analytical thinking and creative approaches to challenges."),
    ("Communication", "Clear articulation of technical concepts."),
    ("Adaptability", " ability to adjust efficiently to new environments."),
    ("Teamwork", "Strong collaboration skills and ability to work effectively."),
]

for col, (skill, desc) in zip(soft_cols, soft_skills):
    with col:
        st.markdown(f"""
        <div style="
            background:#13131f;
            border:1px solid #2a2a3e;
            border-radius:14px;
            padding:1.25rem;
            text-align:center;
        ">
            <p style="color:#00FF89; font-weight:700; font-family:'Syne';">
                {skill}
            </p>
            <p style="color:#6b6b8a; font-size:0.8rem;">
                {desc}
            </p>
        </div>
        """, unsafe_allow_html=True)