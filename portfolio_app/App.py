import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Welcome to My Page | Dindo",
    page_icon="D",
    layout="wide"
)

# ---------------- IMAGE LOADER ----------------
def get_img_base64(relative_path):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, relative_path)

    with open(full_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Example usage (FIXED PATH)
# img = get_img_base64("assest/me.png")

# ---------------- UI ----------------
st.markdown("""
<style>
.stApp {
    background: #000000 !important;
    color: #e8e6f0;
}
</style>
""", unsafe_allow_html=True)

st.title("PORTFOLIO")

# Example image display (optional)
try:
    img = get_img_base64("assest/me.png")

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{img}" width="200"/>
        </div>
        """,
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.error("Image not found. Check folder path: pages/assest/me.png")
