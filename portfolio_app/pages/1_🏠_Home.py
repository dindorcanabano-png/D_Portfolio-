import streamlit as st
import base64
import os

st.set_page_config(page_title="Home | Dindo", page_icon="🏠", layout="wide")

# ================= IMAGE LOADER (FOR YOUR STRUCTURE) =================
def get_img_base64(filename):
    # current file = pages/1_🏠_Home.py
    base_dir = os.path.dirname(__file__)

    # go inside assets folder inside pages
    full_path = os.path.join(base_dir, "assets", filename)

    if not os.path.exists(full_path):
        st.error(f"Image not found: {full_path}")
        return ""

    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ================= LOAD IMAGE =================
img = get_img_base64("me.png")
# =====================================================================


st.markdown("""
<style>
.stApp {
    background: #000000 !important;
    color: white;
}

.logo-badge {
    display:flex;
    justify-content:center;
    align-items:center;
    width:160px;
    height:150px;
    border-radius:20px;
    background:#00FF89;
    padding:3px;
}

.logo-badge img {
    width:100%;
    height:100%;
    border-radius:18px;
    object-fit:cover;
}
</style>
""", unsafe_allow_html=True)


# ================= UI =================
st.markdown("## 🏠 Home Page")

col1, col2 = st.columns([1,3])

with col1:
    if img:
        st.markdown(f"""
        <div class="logo-badge">
            <img src="data:image/png;base64,{img}">
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("### Welcome to my page")
    st.write("Portfolio system running correctly 🚀")
