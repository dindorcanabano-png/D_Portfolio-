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

header, [data-testid="stHeader"] {
    background-color: #000000 !important;
}

[data-testid="stHeader"]::before,
[data-testid="stHeader"]::after {
    display: none !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color:#0F5233;
}

/* TEXT */
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }

/* ================= FLOATING SIDE IMAGE ================= */
.side-avatar {
    position: fixed;
    top: 20px;
    left: 20px;
    width: 90px;
    height: 90px;
    border-radius: 50%;
    z-index: 999;
    animation: float 3s ease-in-out infinite;
    box-shadow: 0 0 25px #00FF89;
    border: 3px solid #00FF89;
}

.side-avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

/* GREEN GLOW ANIMATION */
@keyframes float {
    0% { transform: translateY(0px); box-shadow: 0 0 10px #00FF89; }
    50% { transform: translateY(-10px); box-shadow: 0 0 30px #00FF89; }
    100% { transform: translateY(0px); box-shadow: 0 0 10px #00FF89; }
}

/* LOGO CARD */
.logo-badge {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 160px;
    height: 150px;
    border-radius: 20px;
    background: #00FF89;
    box-shadow: 0 0 20px #00FF89aa;
}

.logo-badge img {
    width: 100%;
    height: 100%;
    border-radius: 18px;
    object-fit: cover;
}

/* CARD */
.metric-card {
    background: rgba(19, 19, 31, 0.8);
    border: 1px solid #00FF8933;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}

/* typing */
.typing-text {
    font-family: 'JetBrains Mono', monospace;
    color: white;
    font-size: 0.85rem;
    white-space: nowrap;
    overflow: hidden;
    border-right: 2px solid #00FF89;
    display: inline-block;
    width: 0;
    animation: typing 5s steps(80, end) infinite, blink 0.7s step-end infinite;
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

# ================= SIDE FLOAT IMAGE =================
if img:
    st.markdown(f"""
    <div class="side-avatar">
        <img src="data:image/png;base64,{img}">
    </div>
    """, unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<h3 style='color:#00FF89;'>[ ACCESSING_CORE_SYSTEM ]</h3>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    if img:
        st.markdown(f"""
        <div class="logo-badge">
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
