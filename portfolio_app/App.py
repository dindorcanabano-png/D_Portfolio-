import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Welcome to My Page | Dindo",
    page_icon="D",
    layout="wide"
)

# ---------------- FIX: IMAGE LOADER (ADDED ONLY) ----------------
def get_img_base64(path):
    full_path = os.path.join(os.path.dirname(__file__), path)

    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---------------- MOBILE DETECTION SCRIPT ----------------
st.markdown("""
<script>
const width = window.innerWidth;
window.parent.postMessage({type: "streamlit:setSessionState", key: "is_mobile", value: width < 768}, "*");
</script>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&display=swap');
.stApp {
    background: #000000 !important;
    color: #e8e6f0;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #e8e6f0;
}
            
section[data-testid="stSidebar"] {
    background: #0F5233 !important;
    border-right: none !important;
}

section[data-testid="stSidebar"] * {
    color: #e8e6f0 !important;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
}

.block-container {
    padding-top: 2rem;
    padding-left: 5%;
    padding-right: 5%;
    max-width: 1400px;
    margin: auto;
}

.logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 180px;
}

.animated-d {
    font-family: 'Syne', sans-serif;
    font-size: clamp(3rem, 8vw, 8rem);
    font-weight: 800;
    color: #021024;
    text-shadow: 0 0 10px #00FF89, 0 0 20px #00FF89;
    animation: pulse 2s infinite alternate;
}

@keyframes pulse {
    from { transform: scale(1); opacity: 0.85; }
    to { transform: scale(1.05); opacity: 1; }
}

hr { border-color: #1e1e2e; }

#MainMenu, footer, header { visibility: hidden; }

.stButton>button {
    width: 100%;
    border-radius: 12px;
}

[data-testid="stHorizontalBlock"] {
    gap: 2rem;
}

.right-panel {
    width: 100%;
}

@media (max-width: 768px) {

    h1 { font-size: 28px !important; text-align: center; }
    h2 { font-size: 22px !important; }
    p { font-size: 14px !important; }

    .logo-container { height: 140px; }

    .animated-d {
        font-size: clamp(2.5rem, 12vw, 5rem);
    }

    .block-container {
        padding-top: 1rem;
        padding-left: 4%;
        padding-right: 4%;
    }

    [data-testid="column"] {
        width: 100% !important;
        flex: 100% !important;
    }

    .element-container {
        text-align: center;
    }

    section[data-testid="stSidebar"] {
        width: 70% !important;
    }
}

@media (min-width: 769px) and (max-width: 1024px) {
    .animated-d {
        font-size: clamp(3rem, 6vw, 6rem);
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
if st.session_state.get("is_mobile", False):
    col_left = st.container()
    col_right = st.container()
else:
    col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("""
<p style='color:#00FF89; font-weight:600; letter-spacing:0.2em; padding-top:2rem; text-align:center;'>
SYSTEM INITIALIZED
</p>
""", unsafe_allow_html=True)

    st.markdown("""
<h1 style="
    font-family:'Syne',sans-serif;
    font-weight:800;
    text-align:center;
    background:#00FF89;
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
">
PORTFOLIO
</h1>
<hr style="border-color:#00FF89; margin-bottom:2rem;">
""", unsafe_allow_html=True)

    st.write("Navigate through the sidebar to explore my technical profile, projects, and career journey.")

    st.markdown("""
<div style="
    background-color:#000000;
    border:1px solid #00FF89;
    border-radius:10px;
    padding:0.8rem 1rem;
    color:#00FF89;
    font-weight:600;
    display:flex;
    align-items:center;
    gap:0.5rem;
">
    <span>⬅</span>
    <span>Use the sidebar to start exploring modules.</span>
</div>
""", unsafe_allow_html=True)

with col_right:
    st.markdown("<div class='right-panel'>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("""
        <div class="logo-container">
            <span class="animated-d">D</span>
        </div>

        <p style='text-align:center; font-family:Syne; font-weight:700; color:#e8e6f0; letter-spacing:0.1em; text-transform:uppercase;'>
            Dindo R. Cañabano
        </p>
        """, unsafe_allow_html=True)

    # ---------------- FIX: IMAGE CALL (ONLY IF YOU USE IT) ----------------
    # If you have this line in your real code, use ONLY this path:
    # img = get_img_base64("assest/me.png")

    st.markdown("</div>", unsafe_allow_html=True)
