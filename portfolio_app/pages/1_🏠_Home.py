import streamlit as st
import base64
import os

st.set_page_config(page_title, page_icon="🏠", layout="wide")

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

/* KEEP STREAMLIT HEADER (NO REMOVAL) */
header {
    background-color: #000000 !important;
}

/* SIDEBAR TEXT WHITE */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* OPTIONAL: sidebar background */
section[data-testid="stSidebar"] {
    background-color:#0F5233;
}

/* MAIN LAYOUT */
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
    margin: auto;
    text-align: center;
}

/* PROFILE WRAPPER */
.profile-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* PROFILE CARD ANIMATION */
.profile-card {
    width: 190px;
    height: 190px;
    border-radius: 16px;
    overflow: hidden;
    background: linear-gradient(45deg, #00FF89, #00ffaa, #00FF89);
    background-size: 300% 300%;
    animation: glowMove 4s ease infinite, floatUp 3s ease-in-out infinite;
    box-shadow: 0 0 25px #00FF89;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.profile-card:hover {
    transform: scale(1.07);
    box-shadow: 0 0 40px #00FF89;
}

.profile-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* ANIMATION */
@keyframes glowMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes floatUp {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* TITLE (BIG + WHITE) */
h1 {
    font-family: 'Syne', sans-serif !important;
    text-align: center !important;
    color: white !important;
    font-size: 1.8rem !important;   /* slightly bigger */
}

/* GREEN LINE LONGER */
hr {
    border: none;
    height: 2px;
    background: #00FF89;
    width: 90%;
    margin: auto;
}

/* CARD */
.metric-card {
    background: rgba(19, 19, 31, 0.85);
    border: 1px solid #00FF8933;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 20px #00FF89;
}

/* MOBILE */
@media (max-width: 768px) {
    .profile-card {
        width: 130px;
        height: 130px;
    }

    h1 {
        font-size: 1.3rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.header("Home | Dindo")  # <-- STREAMLIT HEADER BACK

# ================= PROFILE =================
st.markdown("<div class='profile-wrapper'>", unsafe_allow_html=True)

if img:
    st.markdown(f"""
    <div class="profile-card">
        <img src="data:image/png;base64,{img}">
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("""
<h1>Welcome to my page</h1>
<hr>
""", unsafe_allow_html=True)

# ================= TEXT =================
st.markdown("""
<div style="
    font-family:'JetBrains Mono', monospace;
    color:white;
    font-size:0.85rem;
    text-align:center;
">
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
