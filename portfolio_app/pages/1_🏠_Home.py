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

/* TEXT FONTS */
h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
}

/* ================= SQUARE PROFILE CARD ================= */
.profile-card {
    width: 160px;
    height: 150px;
    margin: auto;
    border-radius: 12px; /* square but slightly soft */
    overflow: hidden;
    background: linear-gradient(45deg, #00FF89, #00ffaa, #00FF89);
    background-size: 300% 300%;
    animation: glowMove 4s ease infinite, float 3s ease-in-out infinite;
    box-shadow: 0 0 25px #00FF89;
}

/* RESPONSIVE PROFILE */
@media (max-width: 768px) {
    .profile-card {
        width: 120px;
        height: 120px;
    }
}

/* IMAGE */
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
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* ================= CARDS ================= */
.metric-card {
    background: rgba(19, 19, 31, 0.8);
    border: 1px solid #00FF8933;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
}

/* HOVER */
.metric-card:hover {
    transform: translateY(-5px);
    border-color: #00FF89;
}

/* ================= CODE TEXT WHITE ================= */
.typing-text {
    font-family: 'JetBrains Mono', monospace;
    color: #ffffff !important;   /* FIXED WHITE */
    font-size: 0.85rem;
    white-space: nowrap;
    overflow: hidden;
    border-right: 2px solid #00FF89;
    display: inline-block;
    width: 100%;
    animation: typing 5s steps(80, end) infinite, blink 0.7s step-end infinite;
}

/* MOBILE FIX */
@media (max-width: 768px) {
    .typing-text {
        font-size: 0.7rem;
        white-space: normal;
        border-right: none;
        animation: none;
    }

    h1 {
        font-size: 1.4rem !important;
        text-align: center;
    }
}

@keyframes typing {
    0% { width: 0ch; }
    50% { width: 80ch; }
    100% { width: 0ch; }
}

@keyframes blink {
    50% { border-color: transparent; }
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<h3 style='color:#00FF89;'>[ ACCESSING_CORE_SYSTEM ]</h3>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    if img:
        st.markdown(f"""
        <div class="profile-card">
            <img src="data:image/png;base64,{img}">
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <h1 style="color:white;">Welcome to my page</h1>
    <hr style="border-color:#00FF89;">
    """, unsafe_allow_html=True)

# ================= TEXT =================
st.markdown("""
<div class="typing-text">
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
            <div style="font-size:1.5rem;">{icon}</div>
            <div style="font-size:2rem;color:#00FF89;font-weight:800;">
                {val}
            </div>
            <div style="color:#00FF89;">
                {label}
            </div>
        </div>
        """, unsafe_allow_html=True)
