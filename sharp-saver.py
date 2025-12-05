import streamlit as st
import streamlit.components.v1 as components
import base64
import random
import os

st.set_page_config(page_title="Sharp Human Experience", page_icon="🏙️", layout="wide")

# --- ASSET LOADER ---
def get_b64_image(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    return None

# --- CONFIGURATION ---
CITY_IMAGE = "sharphuman_color_black-01.jpg"
LOGOS = ["logo1-1.png", "logo1-2.png", "logo1-3.png", "logo1-4.png", "logo1-5.png", "logo1-6.png"]

# Load Background
city_b64 = get_b64_image(CITY_IMAGE)
bg_style = ""
if city_b64:
    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{city_b64}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    /* Hide Streamlit elements for pure immersion */
    header, footer, .stDeployButton {{ display: none !important; }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)
else:
    st.error(f"⚠️ Could not find background image: {CITY_IMAGE}")

# --- ANIMATION ENGINE ---
# We create a swarm of logos with random sizes, speeds, and float paths
particles = []

for _ in range(35): # Number of floating logos
    # Randomize properties
    logo_file = random.choice(LOGOS)
    logo_b64 = get_b64_image(logo_file)
    
    if logo_b64:
        left_pos = random.randint(5, 95)       # Horizontal start
        delay = random.uniform(0, 5)           # Start delay
        duration = random.uniform(8, 15)       # Speed (Slower = more whimsical)
        size = random.randint(40, 120)         # Logo size variability
        sway = random.randint(-50, 50)         # How much it drifts left/right
        
        # HTML for a single logo particle
        html = f"""
        <div style="
            position: fixed;
            left: {left_pos}%;
            bottom: -150px;
            width: {size}px;
            opacity: 0;
            animation: floatWhimsical {duration}s ease-in-out {delay}s infinite;
            filter: drop-shadow(0 0 10px rgba(0, 229, 255, 0.4));
            z-index: 100;
        ">
            <img src="data:image/png;base64,{logo_b64}" style="width: 100%;">
        </div>
        """
        particles.append(html)

# --- CSS KEYFRAMES (The "Whimsical" Movement) ---
# This creates a gentle sway instead of a straight line up
animation_css = """
<style>
@keyframes floatWhimsical {
    0% {
        bottom: -150px;
        transform: translateX(0px) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 0.8;
    }
    50% {
        transform: translateX(30px) rotate(10deg);
    }
    100% {
        bottom: 110vh;
        transform: translateX(-30px) rotate(20deg);
        opacity: 0;
    }
}
</style>
"""

# Render the Magic
full_html = animation_css + "".join(particles)
components.html(full_html, height=0, width=0)

# --- FOREGROUND CONTENT (Optional) ---
# This sits on top of the animation
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True) # Spacer
    st.markdown("""
    <div style="text-align: center; background: rgba(0,0,0,0.7); padding: 40px; border-radius: 20px; border: 1px solid #00e5ff; box-shadow: 0 0 30px rgba(0, 229, 255, 0.2);">
        <h1 style="color: #fff; font-family: Helvetica; font-weight: 100; letter-spacing: 2px;">SHARP HUMAN</h1>
        <p style="color: #00e5ff; font-size: 1.2rem;">ELITE AUTOMATION</p>
    </div>
    """, unsafe_allow_html=True)
