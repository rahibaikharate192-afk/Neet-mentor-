import streamlit as st
import pandas as pd
import json
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="NEET 2027 AI Mentor", page_icon="🩺", layout="wide")

# --- PERSISTENT STATE MANAGEMENT ---
# Initialize session state so data persists while using the app
if "user_data" not in st.session_state:
    st.session_state.user_data = {
        "xp": 0,
        "streak": 0,
        "completed_days": [],
        "syllabus": {
            "Physics": {
                "Motion in 2D": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
                "Laws of Motion": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
                "Work, Energy & Power": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
                "Rotational Motion": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
                "Gravitation": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
            },
            "Chemistry": {
                "Chemical Bonding": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
                "Thermodynamics": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
                "Chemical Equilibrium": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
                "Ionic Equilibrium": {"Lecture": False, "Notes": False, "Module": False, "PYQ": False},
            },
            "Biology": {
                "Cell Cycle & Cell Division": {"Lecture": False, "Notes": False, "Fingertips": False, "NCERT": False},
                "Plant Kingdom": {"Lecture": False, "Notes": False, "Fingertips": False, "NCERT": False},
                "Animal Kingdom": {"Lecture": False, "Notes": False, "Fingertips": False, "NCERT": False},
                "Human Physiology Overview": {"Lecture": False, "Notes": False, "Fingertips": False, "NCERT": False},
            }
        },
        "mock_tests": []
    }

# --- EGO-BASED MOTIVATION ---
def get_ego_motivation():
    quotes = [
        "AIIMS ki seat aaj nahi milti, roz ke discipline se milti hai. Uth aur kaam par lag!",
        "Jab dusre so rahe hain ya scroll kar rahe hain, tab teri AIR decide ho rahi hai.",
        "October tak syllabus khatam karna hai toh aaj ka target har haal me khatam hona chahiye.",
        "Your competition is studying 12 hours today. Are you going to let them take your medical seat?"
    ]
    return quotes[datetime.datetime.now().day % len(quotes)]

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.title("🩺 AI NEET Coach")
st.sidebar.markdown(f"**🔥 Current Streak:** {st.session_state.user_data['streak']} Days")
st.sidebar.markdown(f"**✨ Total XP:** {st.session_state.user_data['xp']}")

page = st.sidebar.radio("Navigate Pages", ["Today's Mission", "Syllabus Tracker", "Test Analytics", "Data Backup"])

# --- PAGE 1: TODAY'S MISSION ---
if page == "Today's Mission":
    st.header("📅 Today's Target & Timetable")
    st.markdown(f"> **🔥 Daily Fuel:** {get_ego_motivation()}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Active Tasks")
        
        # Checking if today is already logged
        today_str = str(datetime.date.today())
        is_done = today_str in st.session_state.user_data["completed_days"]
        
        t1 = st.checkbox("Physics: Next lecture video (Tamanna Mam / Alakh Sir) + 40 Module Qs", disabled=is_done)
        t2 = st.checkbox("Chemistry: Nitesh Devnani Sir lecture + Module concept check", disabled=is_done)
        t3 = st.checkbox("Biology: NCERT deep-read + 80 Fingertips MCQs", disabled=is_done)
        t4 = st.checkbox("Night Revision: Review Mistake Notebook (1.5 Hours)", disabled=is_done)
        
        if is_done:
            st.success("🎉 You already completed today's target! Get some rest or tackle a backlog.")
        else:
            if st.button("Complete Day's Mission"):
                if t1 and t2 and t3 and t4:
                    st.session_state.user_data["xp"] += 100
                    st.session_state.user_data["streak"] += 1
                    st.session_state.user_data["completed_days"].append(today_str)
                    st.success("🔥 100% Target Met! +100 XP added. Keep this momentum rolling.")
                    st.rerun()
                else:
                    st.warning("You must complete every single task before logging the day!")

    with col2:
        st.subheader("🕒 Study Routine (8+ Hours Phase)")
        st.info("""
        *   **06:00 AM - 08:30 AM:** Physics Execution
        *   **09:30 AM - 12:30 PM:** Chemistry (ND Sir Core Concepts)
        *   **02:00 PM - 05:00 PM:** Biology NCERT & Fingertips Drills
        *   **06:00 PM - 08:30 PM:** Mixed Subject Question Practice
        *   **10:00 PM - 11:30 PM:** Night Spaced-Revision Focus
        """)

# --- PAGE 2: SYLLABUS TRACKER ---
elif page == "Syllabus Tracker":
    st.header("📊 Further Completion Tracker")
    st.caption("Tracking what lies ahead. Target Completion: October 2026.")
    
    sub = st.selectbox("Select Subject to Update", ["Physics", "Chemistry", "Biology"])
    
    # Render interactive data editor that feeds straight into session state
    df = pd.DataFrame.from_dict(st.session_state.user_data["syllabus"][sub], orient='index')
    edited_df = st.data_editor(df, use_container_width=True)
    
    # Update the session state dynamically based on user edits
    st.session_state.user_data["syllabus"][sub] = edited_df.to_dict(orient='index')
    st.success("⚡ Track state dynamically updated inside active memory.")

# --- PAGE 3: TEST ANALYTICS ---
elif page == "Test Analytics":
    st.header("📈 Sunday Mock Performance Log")
    
    with st.form("mock_form"):
        t_date = st.date_input("Exam Date", value=datetime.date.today())
        p_m = st.number_input("Physics (Max 180)", 0, 180, 100)
        c_m = st.number_input("Chemistry (Max 180)", 0, 180, 100)
        b_m = st.number_input("Biology (Max 360)", 0, 360, 200)
        
        silly = st.number_input("Silly Errors (Calculation / Bubbling errors)", 0, 45, 0)
        concept = st.number_input("Concept Gaps (Topics you didn't know)", 0, 45, 0)
        
        if st.form_submit_button("Record Performance"):
            total = p_m + c_m + b_m
            log_entry = {"date": str(t_date), "score": total, "silly": silly, "concept": concept}
            st.session_state.user_data["mock_tests"].append(log_entry)
            st.success(f"Score recorded: {total}/720!")
            
    if st.session_state.user_data["mock_tests"]:
        st.subheader("Performance History")
        st.json(st.session_state.user_data["mock_tests"])

# --- PAGE 4: DATA BACKUP ---
elif page == "Data Backup":
    st.header("💾 Keep Your Data Safe (100% Free Storage)")
    st.markdown("""
    Because we are using free hosting tiers, session data resets if the app goes idle for a few hours. 
    **To never lose your streak, download your data file before closing, and upload it when you return!**
    """)
    
    # Convert data state to JSON string for downloading
    json_str = json.dumps(st.session_state.user_data, indent=4)
    st.download_button(
        label="📥 Download Progress File (data.json)",
        data=json_str,
        file_name="neet_progress.json",
        mime="application/json"
    )
    
    st.write("---")
    st.subheader("📤 Upload Progress File")
    uploaded_file = st.file_uploader("Upload your saved neet_progress.json to instantly restore your dashboard configuration:", type=["json"])
    
    if uploaded_file is not None:
        loaded_data = json.load(uploaded_file)
        st.session_state.user_data = loaded_data
        st.success("✅ Dashboard successfully synced back to your latest saved state! Rerun or navigate to start.")
              
