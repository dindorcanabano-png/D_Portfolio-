import streamlit as st
import base64
import os

st.set_page_config(page_title="Home | Dindo", page_icon="🏠", layout="wide")

# ================= IMAGE LOADER =================
def get_img_base64(filename):
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, "assest", filename)

    if not os.path.exists(full_path):
        return ""

    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_img_base64("me.png")

# ================= CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&family=JetBrains+Mono&display=swap');

.stApp {
    background: #000000 !important;
}

/* HEADER */
header, [data-testid="stHeader"] {
    background-color: #000000 !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color:#0F5233;
}

/* ================= RESPONSIVE HEADER TEXT ================= */
.access-text {
    color: #00FF89;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    text-align: center;
    letter-spacing: 2px;
}

/* MOBILE */
@media (max-width: 768px) {
    .access-text {
        font-size: 10px;
    }
}

/* ================= SMALL PROFILE PIC ================= */
.profile-card {
    width: 120px;      /* REDUCED SIZE */
    height: 120px;     /* REDUCED SIZE */
    margin: auto;
    border-radius: 10px;
    overflow: hidden;
    background: linear-gradient(45deg, #00FF89, #00ffaa, #00FF89);
    background-size: 300% 300%;
    animation: glowMove 4s ease infinite, float 3s ease-in-out infinite;
    box-shadow: 0 0 15px #00FF89;
}

/* MOBILE SMALLER */
@media (max-width: 768px) {
    .profile-card {
        width: 90px;
        height: 90px;
    }
}

.profile-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* ANIMATIONS */
@keyframes glowMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
    100% { transform: translateY(0px); }
}

/* ================= TITLE RESPONSIVE ================= */
h1 {
    color: white;
    font-size: clamp(1.2rem, 3vw, 2rem);
    text-align: center;
}

/* ================= SAFE TEXT (NO OVERFLOW) ================= */
.safe-text {
    font-family: 'JetBrains Mono', monospace;
    color: white;
    font-size: 0.8rem;
    text-align: center;

    /* IMPORTANT FIX */
    white-space: normal;
    word-wrap: break-word;
    overflow-wrap: break-word;

    max-width: 100%;
    padding: 0 10px;
}

/* ================= CARDS ================= */
.metric-card {
    background: rgba(19, 19, 31, 0.8);
    border: 1px solid #00FF8933;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
}

/* MOBILE CARDS */
@media (max-width: 768px) {
    .metric-card {
        padding: 10px;
    }
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<div class='access-text'>[ ACCESSING_CORE_SYSTEM ]</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 5])

with col1:
    if img:
        st.markdown(f"""
        <div class="profile-card">
            <img src="data:image/png;base64,{img}">
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <h1>Welcome to my page</h1>
    <hr style="border-color:#00FF89;">
    """, unsafe_allow_html=True)

# ================= SAFE TEXT (NO OVERFLOW FIXED) =================
st.markdown("""
<div class="safe-text">
You can copy the output, but without understanding the logic, it won’t last.
</div>
""", unsafe_allow_html=True)

st.divider()

# ================= STATS =================
stats = [
    ("PROJECTS", "3+", "⚡"),
    ("EXPERIENCE", "2 YRS", "🏆"),
    ("CLIENTS", "01+", "🤝"),
    ("SYSTEM_UP", "99.9%", "⚙️")
]

cols = st.columns(4)

for i, (label, val, icon) in enumerate(stats):
    with cols[i]:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size:1.2rem;">{icon}</div>
            <div style="font-size:1.5rem;color:#00FF89;font-weight:800;">
                {val}
            </div>
            <div style="color:#00FF89;font-size:0.75rem;">
                {label}
            </div>
        </div>
        """, unsafe_allow_html=True)
