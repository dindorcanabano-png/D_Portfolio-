import streamlit as st

st.title(" Welcome to My Portfolio")
st.write(""" """)

st.success("Simple Portfolio Multipage App using Streamlit ")

st.markdown("""
<script>
const width = window.innerWidth;
window.parent.postMessage({type: "streamlit:setSessionState", key: "is_mobile", value: width < 768}, "*");
</script>
""", unsafe_allow_html=True)

# CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&display=swap');

/* GENERAL */
.stApp {
    background: #000000 !important;
    color: #e8e6f0;
}

header, [data-testid="stHeader"] {
    background-color: #000000 !important;
}

#MainMenu, footer { visibility: hidden; }

/* FONTS */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #e8e6f0;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
}

/* LAYOUT */
.block-container {
    padding-top: 2rem;
    padding-left: 5%;
    padding-right: 5%;
    max-width: 1400px;
    margin: auto;
}

/* LOGO */
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

</style>
""", unsafe_allow_html=True)

# HEADER
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

# MAIN CONTENT
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
