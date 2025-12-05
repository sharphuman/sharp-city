import streamlit as st
import streamlit.components.v1 as components
import base64
import random
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="Sharp Human Experience", page_icon="🏙️", layout="wide")

# --- ASSET LOADER ---
def get_b64_image(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    return None

# --- CONFIGURATION ---
# Use the exact filenames you uploaded
CITY_IMAGE = "sharphuman_color_black-01.jpg"
LOGOS = [
    "logo1-1.png", "logo1-2.png", "logo1-3.png", 
    "logo1-4.png", "logo1-5.png", "logo1-6.png"
]

# --- BACKGROUND SETUP ---
city_b64 = get_b64_image(CITY_IMAGE)

if city_b64:
    # If image is found, use it
    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{city_b64}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
else:
    # Fallback if image missing: Deep Black
    st.warning(f"⚠️ Image not found: {CITY_IMAGE}. Using black background.")
    bg_css = """
    <style>
    .stApp { background-color: #0e1117; }
    </style>
    """

# Hide Streamlit UI elements for immersion
bg_css += """
<style>
header, footer, .stDeployButton { display: none !important; }
</style>
"""
st.markdown(bg_css, unsafe_allow_html=True)

# --- ANIMATION ENGINE ---
particles = []

# Generate 35 floating logos
for _ in range(35):
    # Pick a random logo file
    logo_file = random.choice(LOGOS)
    logo_b64 = get_b64_image(logo_file)
    
    if logo_b64:
        left_pos = random.randint(5, 95)       # Horizontal start
        delay = random.uniform(0, 8)           # Random delay start
        duration = random.uniform(10, 20)      # Slow, floaty speed
        size = random.randint(50, 100)         # Logo size variability
        
        # HTML for a single logo particle
        # Uses 'drop-shadow' to make them glow against the dark city
        html = f"""
        <div style="
            position: fixed;
            left: {left_pos}%;
            bottom: -150px;
            width: {size}px;
            opacity: 0;
            animation: floatWhimsical {duration}s ease-in-out {delay}s infinite;
            filter: drop-shadow(0 0 10px rgba(0, 229, 255, 0.6));
            z-index: 100;
            pointer-events: none;
        ">
            <img src="data:image/png;base64,{logo_b64}" style="width: 100%;">
        </div>
        """
        particles.append(html)

# --- KEYFRAMES (The "Whimsical" Sway) ---
animation_css = """
<style>
@keyframes floatWhimsical {
    0% {
        bottom: -150px;
        transform: translateX(0px) rotate(0deg) scale(0.8);
        opacity: 0;
    }
    10% {
        opacity: 0.9;
    }
    33% {
        transform: translateX(40px) rotate(15deg) scale(1);
    }
    66% {
        transform: translateX(-40px) rotate(-15deg) scale(1);
    }
    100% {
        bottom: 110vh;
        transform: translateX(20px) rotate(10deg) scale(0.8);
        opacity: 0;
    }
}
</style>
"""

# Render the Magic
full_html = animation_css + "".join(particles)
components.html(full_html, height=0, width=0)

# --- FOREGROUND TITLE (Optional Overlay) ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        text-align: center; 
        background: rgba(0,0,0,0.6); 
        padding: 40px; 
        border-radius: 20px; 
        border: 1px solid rgba(0, 229, 255, 0.3); 
        backdrop-filter: blur(5px);
        box-shadow: 0 0 50px rgba(0, 229, 255, 0.1);
    ">
        <h1 style="
            color: #fff; 
            font-family: 'Helvetica Neue', sans-serif; 
            font-weight: 100; 
            letter-spacing: 4px;
            text-transform: uppercase;
            margin: 0;
        ">Sharp Human</h1>
        <p style="
            color: #00e5ff; 
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 1rem; 
            letter-spacing: 2px;
            margin-top: 10px;
        ">Elite Automation</p>
    </div>
    """, unsafe_allow_html=True)
