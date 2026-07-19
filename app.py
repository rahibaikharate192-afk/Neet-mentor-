import streamlit as st
import datetime

# Page Configurations
st.set_page_config(page_title="AI NEET Mentor 2027", page_icon="🩺", layout="wide")

# Custom Aggressive Ego Motivation Logic based on time of day
now = datetime.datetime.now()
current_hour = now.hour

if current_hour < 12:
    greeting = "Waking up late isn't an option for someone with a 300-score chip on their shoulder. Prove them wrong today."
elif 12 <= current_hour < 18:
    greeting = "The competition is sitting in an air-conditioned room solving modules right now. Are you coasting, or are you executing?"
else:
    greeting = "The sun is down. This is where the real medical seats are earned. Sleep only when the targets are dead."

# --- SIDEBAR: PROGRESS & ACCOUNTABILITY ---
st.sidebar.title("🩺 AI COMMAND CENTER")
st.sidebar.markdown(f"**Mentor Status:** 🟢 Active & Monitoring")
st.sidebar.markdown("---")

# Deadline Calculator to Oct 31st
syllabus_deadline = datetime.date(2026, 10, 31)
days_left = (syllabus_deadline - datetime.date.today()).days
st.sidebar.metric(label="Days to Complete Syllabus", value=f"{days_left} Days")

# Momentum Slider (Switches between 8hr and 12hr schedules)
momentum = st.sidebar.select_slider(
    "Select Your Current Momentum Phase:",
    options=["8-Hour Foundation", "12-Hour Absolute Grind"]
)

# --- MAIN DASHBOARD ---
st.title("Welcome to Your AI NEET Mentor Dashboard")
st.error(f"🔥 **EGO CHECK:** {greeting}")

st.markdown("---")

# Layout: Two Main Blocks
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🎯 Today's Dynamic Targets")
    
    if momentum == "8-Hour Foundation":
        st.info("💡 Phase: Building Momentum. Focus heavily on clearing backlogged question banks.")
        st.checkbox("⚡ Physics (3 Hours): Tamanna Choudhary Lec / Backlog Practice (Errorless/IIB)")
        st.checkbox("🧪 Chemistry (3 Hours): ND Sir Lecture + Module Questions")
        st.checkbox("🌿 Biology (2 Hours): NCERT Line-by-Line + Fingertips Active Recall")
    else:
        st.warning("🚀 Phase: Hyper-Drive Mode active. 12 Hours Clocking Required.")
        st.checkbox("⚡ Physics (4.5 Hours): Double-down on Kinematics/Mechanics Modules (Allen/IIB)")
        st.checkbox("🧪 Chemistry (4.5 Hours): Physical/Inorganic Balaji Reference problems")
        st.checkbox("🌿 Biology (3 Hours): High-volume NCERT Fingertips MCQ drilling")

    # Task Completer Button
    st.markdown("###")
    if st.button("🔴 Day Complete - Submit Tasks for Review"):
        st.balloons()
        st.success("AI Mentor: Data logged. Preparing tomorrow's shift based on your performance speed.")

with col2:
    st.header("📊 Sunday Test Analyzer")
    st.write("Input your latest Sunday Part-Test results to recalibrate the system:")
    
    phy_score = st.number_input("Physics Score", min_value=0, max_value=180, value=100)
    chem_score = st.number_input("Chemistry Score", min_value=0, max_value=180, value=100)
    bio_score = st.number_input("Biology Score", min_value=0, max_value=360, value=200)
    
    if st.button("Analyze Test Scores"):
        total = phy_score + chem_score + bio_score
        st.metric(label="Total Test Score", value=f"{total} / 720")
        
        # Mentor Feedback Prompting
        if total < 500:
            st.error("AI Mentor Review: Your question processing speed is lacking. The database will automatically increase the weight of high-yield practice modules for your upcoming weekly planner.")
        else:
            st.success("AI Mentor Review: Moving in the right direction. Keep this intensity up.")

st.markdown("---")
st.header("📁 Chapter Matrix & Resource Tracker")

# Multi-select trackers to show what resources are tapped out per chapter
subject_tab1, subject_tab2, subject_tab3 = st.tabs(["Physics", "Chemistry", "Biology"])

with subject_tab1:
    st.markdown("### Kinematics / Mechanics Tracker")
    st.multiselect(
        "Select completed layers for 'Motion in 1D':",
        ["Tamanna Choudhary / Alakh Sir Lecture", "IIB Notes", "PYQs", "Errorless Book", "Allen/IIB Module"],
        default=["Tamanna Choudhary / Alakh Sir Lecture", "IIB Notes"]
  )
