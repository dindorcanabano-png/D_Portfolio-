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

/* CENTER MAIN LAYOUT */
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
    margin: auto;
    text-align: center;
}

header, [data-testid="stHeader"] {
    background-color: #000000 !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color:#0F5233;
}

/* TEXT */
h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
    text-align: center !important;
}

/* ACCESS TEXT */
.access-text {
    color: #00FF89;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    letter-spacing: 2px;
    text-align: center;
}

/* PROFILE WRAPPER */
.profile-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* PROFILE CARD */
.profile-card {
    width: 190px;
    height: 190px;
    border-radius: 16px;
    overflow: hidden;
    background: linear-gradient(45deg, #00FF89, #00ffaa, #00FF89);
    background-size: 300% 300%;
    animation: glowMove 4s ease infinite;
    box-shadow: 0 0 25px #00FF89;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

/* CLEAN HOVER (NO LAYOUT BREAK) */
.profile-card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 35px #00FF89;
}

/* IMAGE */
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

/* CARD */
.metric-card {
    background: rgba(19, 19, 31, 0.85);
    border: 1px solid #00FF8933;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    transition: transform 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
}

/* MOBILE */
@media (max-width: 768px) {
    .profile-card {
        width: 130px;
        height: 130px;
    }

    .access-text {
        font-size: 11px;
    }
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<div class='access-text'>[ ACCESSING_CORE_SYSTEM ]</div>", unsafe_allow_html=True)

# FULL CENTER LAYOUT (NO SIDE SHIFT)
st.markdown("<div class='profile-wrapper'>", unsafe_allow_html=True)

if img:
    st.markdown(f"""
    <div class="profile-card">
        <img src="data:image/png;base64,{img}">
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<h1>Welcome to my page</h1>
<hr style="border-color:#00FF89; width:60%; margin:auto;">
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
