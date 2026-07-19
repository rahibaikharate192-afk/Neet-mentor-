import streamlit as st
import pandas as pd
import json
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="NEET 2027 AI Mentor", page_icon="🩺", layout="wide")

# --- INITIAL DATA STRUCTURES ---
# Chapters you have already completed (Practice Pending)
initial_completion = {
    "Physics": {
        "Units & Dimensions": {"Lecture": True, "Notes": True, "Module": False, "PYQ": False},
        "Errors & Measurements": {"Lecture": True, "Notes": True, "Module": False, "PYQ": False},
        "Motion in 1D": {"Lecture": True, "Notes": True, "Module": False, "PYQ": False},
    },
    "Chemistry": {
        "Mole Concept": {"Lecture": True, "Notes": True, "Module": False, "PYQ": False},
        "Atomic Structure": {"Lecture": True, "Notes": True, "Module": False, "PYQ": False},
    },
    "Biology": {
        "Cell: The Unit of Life": {"Lecture": True, "Notes": True, "Fingertips": False, "NCERT": True},
        "Biomolecules": {"Lecture": True, "Notes": True, "Fingertips": False, "NCERT": True},
    }
}

# --- EGO-BASED MOTIVATION GENERATOR ---
def get_ego_motivation():
    quotes = [
        "AIIMS ki seat aaj nahi milti, roz ke discipline se milti hai. Uth aur kaam par lag.",
        "Jab dusre so rahe hain ya scroll kar rahe hain, tab teri AIR decide ho rahi hai.",
        "October tak syllabus khatam karna hai toh aaj ka target har haal me khatam hona chahiye.",
        "Your competition is studying 13 hours today. Are you going to let them take your seat?"
    ]
    # Simple rotation based on day of the month
    return quotes[datetime.datetime.now().day % len(quotes)]

# --- MAIN DASHBOARD UI ---
st.title("🩺 NEET 2027 Personalized AI Coach")
st.markdown(f"> **🔥 Daily Fuel:** {get_ego_motivation()}")

# Sidebar Navigation
page = st.sidebar.radio("Navigate", ["Today's Mission", "Subject Tracker", "Test Performance", "Backlog & Revision"])

# --- PAGE 1: TODAY'S MISSION ---
if page == "Today's Mission":
    st.header("📅 Today's Target & Timetable")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Active Tasks")
        t1 = st.checkbox("Physics: Complete Question Practice for pending chapters (80 Questions)")
        t2 = st.checkbox("Chemistry: Next organic/inorganic lecture + Shri Balaji reference problems")
        t3 = st.checkbox("Biology: NCERT deep-read + Fingertips questions (100 MCQ)")
        t4 = st.checkbox("Night Revision: Review Mistake Notebook (1.5 Hours)")
        
        if st.button("Complete Day's Mission & Calculate XP"):
            if t1 and t2 and t3 and t4:
                st.success("🔥 100% Consistency Streak Maintained! +100 XP added to your dashboard.")
            else:
                st.warning("Finish all tasks to claim today's streak score!")

    with col2:
        st.subheader("🕒 Current Phase: 8+ Hours Schedule")
        st.info("""
        *   **06:00 AM - 08:30 AM:** Physics Application & Modules
        *   **09:30 AM - 12:30 PM:** Chemistry Video Lectures (ND Sir) & Notes
        *   **02:00 PM - 05:00 PM:** Biology NCERT Intensive & Fingertips
        *   **06:00 PM - 08:30 PM:** Physics PYQs / Revision
        *   **10:00 PM - 11:30 PM:** Night Spaced-Revision Cycle
        """)

# --- PAGE 2: SUBJECT TRACKER ---
elif page == "Subject Tracker":
    st.header("📊 Interactive Syllabus Tracker")
    st.caption("Target: 100% Completion by October")
    
    subject = st.selectbox("Choose Subject", ["Physics", "Chemistry", "Biology"])
    
    if subject == "Physics":
        st.write("**Mentors:** Tamanna Choudhary (Main) / Alakh Sir (Tough Chapters)")
        st.write("**Resources:** IIB Notes, IIB Module, Allen Module, Errorless, PYQs")
        
        # Display sample status table
        df = pd.DataFrame.from_dict(initial_completion["Physics"], orient='index')
        st.data_editor(df, use_container_width=True)
        
    elif subject == "Chemistry":
        st.write("**Mentors:** Nitesh Devnani Sir")
        st.write("**Resources:** IIB Notes, Modules, Shri Balaji Reference")
        df = pd.DataFrame.from_dict(initial_completion["Chemistry"], orient='index')
        st.data_editor(df, use_container_width=True)
        
    elif subject == "Biology":
        st.write("**Resources:** NCERT Textbook, NCERT Fingertips, IIB Notes")
        df = pd.DataFrame.from_dict(initial_completion["Biology"], orient='index')
        st.data_editor(df, use_container_width=True)

# --- PAGE 3: TEST PERFORMANCE ---
elif page == "Test Performance":
    st.header("📈 Sunday Mock Test Analytics")
    
    with st.form("test_entry"):
        test_date = st.date_input("Test Date")
        p_score = st.number_input("Physics Score (Max 180)", min_value=0, max_value=180, value=100)
        c_score = st.number_input("Chemistry Score (Max 180)", min_value=0, max_value=180, value=100)
        b_score = st.number_input("Biology Score (Max 360)", min_value=0, max_value=360, value=200)
        
        st.subheader("⚠️ Error Analysis")
        silly_mistakes = st.number_input("Silly Mistakes (Calculation/Bubbling)", min_value=0)
        concept_gaps = st.number_input("Concept Gaps (Didn't know the logic)", min_value=0)
        
        submitted = st.form_submit_form("Analyze Performance")
        if submitted:
            total = p_score + c_score + b_score
            st.metric(label="Total Score", value=f"{total} / 720", delta=f"{total - 300} compared to previous baseline")
            
            if silly_mistakes > 4:
                st.error(f"🛑 You lost {silly_mistakes * 5} marks just on accuracy. Slow down during question reading!")
            else:
                st.success("Great accuracy control!")

