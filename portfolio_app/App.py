import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Welcome to My Page | Dindo",
    page_icon="D",
    layout="wide"
)

# ---------------- IMAGE LOADER (FIXED SAFE VERSION) ----------------
def get_img_base64(path):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Image not found: {full_path}")

    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---------------- MOBILE DETECTION SCRIPT ----------------
# FIX: Streamlit cannot directly read JS -> removed breaking behavior but kept structure
st.markdown("""
<script>
const width = window.innerWidth;
window.parent.postMessage({type: "streamlit:setSessionState", key: "is_mobile", value: width < 768}, "*");
</script>
""", unsafe_allow_html=True)

# ---------------- CSS ----------------
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
    color: #00FF89;
    text-shadow: 0 0 10px #00FF89, 0 0 20px #00FF89;
    animation: pulse 2s infinite alternate;
}

@keyframes pulse {
    from { transform: scale(1); opacity: 0.85; }
    to { transform: scale(1.05); opacity: 1; }
}

hr { border-color: #00FF89; }

#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
is_mobile = st.session_state.get("is_mobile", False)

if is_mobile:
    col_left = st.container()
    col_right = st.container()
else:
    col_left, col_right = st.columns([2, 1])

# ---------------- LEFT SIDE ----------------
with col_left:
    st.markdown("""
<p style='color:#00FF89; font-weight:600; letter-spacing:0.2em; text-align:center;'>
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
<hr>
""", unsafe_allow_html=True)

    st.write("Navigate through the sidebar to explore my technical profile, projects, and career journey.")

# ---------------- RIGHT SIDE ----------------
with col_right:
    st.markdown("<div class='right-panel'>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class="logo-container">
            <span class="animated-d">D</span>
        </div>

        <p style='text-align:center; font-family:Syne; font-weight:700;'>
            Dindo R. Cañabano
        </p>
        """, unsafe_allow_html=True)

    # ---------------- IMAGE (FIXED SAFELY) ----------------
    try:
        img = get_img_base64("assest/me.png")

        st.markdown(
            f"""
            <div style="text-align:center; margin-top:20px;">
                <img src="data:image/png;base64,{img}" width="200"/>
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Image error: {e}")

    st.markdown("</div>", unsafe_allow_html=True)
