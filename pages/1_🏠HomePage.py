import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AI Job Salary Predictor",
    page_icon="🏠",
    layout="wide"
)

# --- HEADER IMAGE ---
st.image("ai.png", use_column_width=True)

# --- TITLE & INTRO ---
st.title("🏠 Welcome to the AI Job Salary Prediction Dashboard")
st.markdown("""
This interactive dashboard helps you **explore global AI job market trends** and 
**predict salaries** using data science.  
Whether you're a data enthusiast, job seeker, or HR analyst — this tool gives you real-time insights into the world of tech careers.
""")

# --- DIVIDER ---
st.divider()

# --- FEATURE OVERVIEW ---
st.subheader("✨ What You Can Do Here")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Job Market Insights")
    st.write("""
    Explore visual analytics on job trends, company sizes, 
    experience levels, and education requirements.
    """)

with col2:
    st.markdown("### 🤖 Salary Prediction")
    st.write("""
    Input job-related information to predict your estimated 
    salary using our trained AI model.
    """)


# --- CALL TO ACTION ---
st.divider()
st.markdown("""
### 🚀 Ready to explore?
Use the sidebar on the **left** to navigate through different sections of the app.  
""")


