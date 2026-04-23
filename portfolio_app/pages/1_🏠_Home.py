import streamlit as st
import base64
import os


st.set_page_config(page_title="Home | Dindo", page_icon="🏠", layout="wide")

def get_img_base64(path):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Image not found at: {full_path}")

    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


img = get_img_base64("assest/me.png")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&family=JetBrains+Mono&display=swap');

/* BACKGROUND */
.stApp {
    background: #000000 !important;
}
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

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color:#0F5233;
    border-right: 1px solid #1e1e2e;
}

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* FONTS */
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }
p, span { font-family: 'DM Sans', sans-serif; }

/* LOGO */
.logo-badge {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 160px;
    height: 150px;
    border-radius: 20px;
    background: linear-gradient(135deg, #00FF89, #00FF89);
    padding: 3px;
    box-shadow: 0 0 20px #00FF89aa;
    animation: floatGlow 3s ease-in-out infinite;
}

.logo-badge img {
    width: 100%;
    height: 100%;
    border-radius: 18px;
    object-fit: cover;
}

@keyframes floatGlow {
    0% { transform: translateY(0px) scale(1); }
    50% { transform: translateY(-8px) scale(1.05); }
    100% { transform: translateY(0px) scale(1); }
}

/* CARD */
.metric-card {
    background: rgba(19, 19, 31, 0.8);
    border: 1px solid #00FF8933;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}

/* TERMINAL TEXT */
.terminal-code {
    font-family: 'JetBrains Mono', monospace;
    color: #00FF89;
}

/* FOOTER */
footer {
    visibility: visible !important;
    background-color: black !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<p class='terminal-code'>[ ACCESSING_CORE_SYSTEM ]</p>", unsafe_allow_html=True)

col_logo, col_title = st.columns([1, 4])

with col_logo:
    st.markdown(f"""
    <div class="logo-badge">
        <img src="data:image/png;base64,{img}">
    </div>
    """, unsafe_allow_html=True)

with col_title:
    st.markdown("""
    <h1 style="
        font-family:'Syne',sans-serif;
        font-size:clamp(1.8rem, 4vw, 2.6rem);
        font-weight:800;
        background:white;
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    ">
    Welcome to my page
    </h1>
    <hr style="border-color:#00FF89;">
    """, unsafe_allow_html=True)
