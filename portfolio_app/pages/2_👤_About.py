import streamlit as st
from pathlib import Path

st.set_page_config(page_title="About Me", page_icon="🧑‍💻", layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent

cert1 = BASE_DIR / "pages/assest/cert1.png"
cert2 = BASE_DIR / "pages/assest/cert2.jpg"
cert3 = BASE_DIR / "pages/assest/cert3.jpg"
cert4 = BASE_DIR / "pages/assest/cert4.png"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

.stApp {
    background-color: #000000!important;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #e8e6f0;
}

#MainMenu, footer, header { visibility: hidden; }

/* SIDEBAR */
[data-testid="stSidebar"] {
    background:#0F5233;
    border-right: 1px solid #1e1e2e;
}
            
section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif;
    letter-spacing: -0.02em;
}

hr { border-color: #1e1e2e; }

img {
    border-radius: 12px;
}
/* CERT TITLE FIX (NO OVERLAP) */
.cert-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    margin-top: 2rem;
    margin-bottom: 1.5rem;
    text-align: center;

    background: linear-gradient(135deg, #e8e6f0 40%, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    position: relative;
    z-index: 10;
}

/* CERT CARD */
.cert-card {
    background: #13131f;
    border: 1px solid #2a2a3e;
    border-radius: 14px;
    padding: 10px;
    transition: all 0.3s ease-in-out;
    overflow: hidden;
    text-align: center;
}

/* IMAGE */
.cert-card img {
    width: 100%;
    border-radius: 10px;
    transition: transform 0.3s ease-in-out;
}

/* LABEL (THIS FIXES “WORDS DISAPPEARING”) */
.cert-label {
    margin-top: 8px;
    color: #e8e6f0;
    font-size: 0.8rem;
    font-family: 'DM Sans', sans-serif;
}

/* HOVER EFFECT */
.cert-card:hover {
    transform: translateY(-8px) scale(1.03);
    border-color: #00FF89;
    box-shadow: 0 0 20px rgba(0,255,137,0.25);
}

.cert-card:hover img {
    transform: scale(1.08);
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
    padding-top: 1.5rem;
    margin-bottom:0.5rem;
">Get To Know Me</p>

<h1 style="
    font-family:'Syne',sans-serif;
    font-size:3rem;  /* 🔥 BIGGER */
    font-weight:800;
    background: linear-gradient(135deg, #e8e6f0 40%, #a78bfa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:0.25rem;
">About Me</h1>

<hr style="border-color:#00FF89; margin-bottom:2rem;">
""", unsafe_allow_html=True)

col_bio, col_info = st.columns([1.5, 1], gap="large")

with col_bio:
    st.markdown("""
    <div style="
        background:#13131f; border:1px solid #2a2a3e; border-radius:16px;
        padding:1.75rem 2rem; margin-bottom:1.25rem;
    ">
        <p style="font-family:'Syne',sans-serif; font-weight:700;
                  color:#00FF89; font-size:1rem; margin-bottom:0.75rem;">
            Who I Am
        </p>
        <p style="color:#b0afc8; line-height:1.8; font-size:0.95rem;">
            I'm Dindo, a driven Computer Science student with a passion for
            building functional and impactful software. I thrive at the
            intersection of <strong style="color:#e8e6f0;">design and programming</strong>.
        </p>
        <p style="color:#b0afc8; line-height:1.8; font-size:0.95rem; margin-top:1rem;">
            Whether it's building apps, designing UI, or solving logic problems,
            I always bring curiosity and dedication.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="font-family:'Syne',sans-serif; font-weight:700;
              color:#00FF89; font-size:1rem; margin:1.5rem 0 1rem;">
        Education Timeline
    </p>
    """, unsafe_allow_html=True)

    timeline_items = [
        ("2024", "Hackathon Participant",
         "Participated in a hackathon contributing to visuals and presentation."),
        ("2025", "Hackathon Team Member",
         "Continued participation as a defender in the event of bank hacking."),
        ("2026", "Student Programmer / Editor",
         "Currently studying programming and doing editing tasks.")
    ]

    for year, title, desc in timeline_items:
        st.markdown(f"""
        <div style="display:flex; gap:1rem; margin-bottom:1rem;">
            <div style="min-width:64px; text-align:right;">
                <span style="color:#00FF89; font-weight:700;">{year}</span>
            </div>
            <div style="width:10px; height:10px; border-radius:50%;
                        background:#00FF89; margin-top:4px;"></div>
            <div style="background:#13131f; border:1px solid #2a2a3e;
                        border-radius:10px; padding:0.9rem; flex:1;">
                <p style="color:#e8e6f0; font-weight:700; margin:0;">{title}</p>
                <p style="color:#6b6b8a; font-size:0.82rem; margin:0;">{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col_info:
    st.markdown("""
    <div style="background:#13131f; border:1px solid #2a2a3e;
                border-radius:16px; padding:1.75rem;">
        <p style="color:#00FF89; font-weight:700;">Quick Info</p>
    """, unsafe_allow_html=True)

    info_items = [
        ("Role", "Student Developer"),
        ("Degree", "Computer Science"),
        ("Focus", "Full-Stack Development"),
        ("Location", "Philippines"),
        ("Status", "Open to Opportunities"),
    ]

    for label, value in info_items:
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between;
                    padding:0.5rem 0; border-bottom:1px solid #1e1e2e;">
            <span style="color:#6b6b8a;">{label}</span>
            <span style="color:#e8e6f0;">{value}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='cert-title'>Certificates</div>", unsafe_allow_html=True)

certs = [
    (cert1, "Certificate 1"),
    (cert2, "Certificate 2"),
    (cert3, "Certificate 3"),
    (cert4, "Certificate 4")
]

col1, col2, col3, col4 = st.columns(4)

for col, (cert, title) in zip([col1, col2, col3, col4], certs):
    with col:
        st.markdown(f"""
        <div class="cert-card">
            <img src="data:image/png;base64,{__import__('base64').b64encode(open(cert, 'rb').read()).decode()}" />
            <p class="cert-label">{title}</p>
        </div>
        """, unsafe_allow_html=True)