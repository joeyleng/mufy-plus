import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ---------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Student Diary Counsellor",
    page_icon="🌈",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown(
    """
    <style>

    .main {
        background: linear-gradient(to bottom right, #f5f7ff, #e8f0ff);
    }

    .title {
        text-align: center;
        color: #3b3b98;
        font-size: 50px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #555;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    .ai-box {
        background: linear-gradient(to right, #dfe9ff, #edf3ff);
        padding: 15px;
        border-radius: 15px;
        border-left: 6px solid #4c6ef5;
        margin-top: 15px;
    }

    .mood-box {
        background: linear-gradient(to right, #fff0f6, #ffe3ec);
        padding: 10px;
        border-radius: 12px;
        text-align: center;
        font-size: 20px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# TITLE SECTION
# ---------------------------------------------------
st.markdown("<div class='title'>📘 AI Student Diary Counsellor</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>A safe and supportive digital space for students to manage stress, emotions, and daily challenges.</div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# HEADER IMAGE
# ---------------------------------------------------
st.image(
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
    use_container_width=True
)

# ---------------------------------------------------
# FILE SETUP
# ---------------------------------------------------
FILE_NAME = "student_diary_entries.csv"

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Time", "Mood", "Diary", "AI Response"])
    df.to_csv(FILE_NAME, index=False)

entries_df = pd.read_csv(FILE_NAME)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("🌈 Wellness Corner")

st.sidebar.image(
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    use_container_width=True
)

st.sidebar.info(
    "Remember: Your mental health matters. Take breaks, drink water, sleep well, and ask for help when needed."
)

st.sidebar.success("✨ Daily Motivation: Small progress is still progress.")

# ---------------------------------------------------
# AI COUNSELLOR
# ---------------------------------------------------
def ai_counsellor_response(text, mood):

    text = text.lower()

    if "stress" in text or "exam" in text:
        return (
            "📚 Exams and school pressure can feel overwhelming, but you are stronger than you think. "
            "Try creating a study schedule, taking short breaks, and rewarding yourself after completing tasks. "
            "Remember that one difficult day does not define your future."
        )

    elif "sad" in text or "cry" in text or "depressed" in text:
        return (
            "💙 I am sorry you are feeling this way. Your feelings are valid and important. "
            "Please remember that you do not need to go through difficult emotions alone. "
            "Talking to someone you trust can help lighten emotional pressure."
        )

    elif "anxiety" in text or "worried" in text or "panic" in text:
        return (
            "🌿 Anxiety can make situations feel bigger than they are. "
            "Take a deep breath and focus on one thing at a time. "
            "You can try journaling, listening to calming music, or practicing mindfulness exercises."
        )

    elif "lonely" in text:
        return (
            "🤝 Feeling lonely can be painful, but remember that connection takes time. "
            "Try reaching out to a friend, family member, teacher, or support group. "
            "You deserve support and kindness."
        )

    elif "tired" in text or "burnout" in text:
        return (
            "😴 You may be experiencing burnout. Rest is not laziness — it is important self-care. "
            "Take time to recharge your mind and body."
        )

    elif mood == "Happy 😊":
        return (
            "✨ It is wonderful to hear positive energy in your day. "
            "Keep celebrating your achievements and continue spreading positivity around you."
        )

    else:
        return (
            "🌈 Thank you for sharing your thoughts today. "
            "Every emotion you experience matters, and expressing yourself is a healthy step toward emotional wellness."
        )

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------
col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("## 📝 Daily Diary Entry")

    mood = st.selectbox(
        "Select your mood today:",
        [
            "Happy 😊",
            "Sad 😢",
            "Stressed 😰",
            "Anxious 😟",
            "Excited 🤩",
            "Tired 😴"
        ]
    )

    diary_text = st.text_area(
        "Write about your day:",
        height=220,
        placeholder="Share your feelings, school experiences, stress, or anything on your mind..."
    )

    if st.button("💾 Save Diary Entry"):

        if diary_text.strip() == "":
            st.warning("Please write something before submitting.")

        else:
            response = ai_counsellor_response(diary_text, mood)

            new_entry = {
                "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Mood": mood,
                "Diary": diary_text,
                "AI Response": response
            }

            entries_df = pd.concat(
                [entries_df, pd.DataFrame([new_entry])],
                ignore_index=True
            )

            entries_df.to_csv(FILE_NAME, index=False)

            st.success("✅ Your diary entry has been saved successfully.")

            st.markdown("### 🤖 AI Counsellor Response")
            st.markdown(f"<div class='ai-box'>{response}</div>", unsafe_allow_html=True)

with col2:

    st.markdown("## 🌟 Mental Wellness Tips")

    st.image(
        "https://images.unsplash.com/photo-1494790108377-be9c29b29330",
        use_container_width=True
    )

    st.markdown(
        """
        ### Healthy Habits

        - 💤 Sleep at least 7–8 hours
        - 💧 Drink enough water
        - 🚶 Exercise regularly
        - 📚 Study in small sessions
        - 🎵 Listen to calming music
        - 🧘 Practice mindfulness
        """
    )

# ---------------------------------------------------
# PREVIOUS ENTRIES
# ---------------------------------------------------
st.markdown("---")
st.markdown("# 📚 Previous Diary Entries")

if not entries_df.empty:

    reverse_df = entries_df.iloc[::-1]

    for _, row in reverse_df.iterrows():

        with st.expander(f"📅 {row['Time']} | {row['Mood']}"):

            st.markdown(
                f"<div class='mood-box'>Mood: {row['Mood']}</div>",
                unsafe_allow_html=True
            )

            st.write("### 📝 Diary Entry")
            st.write(row['Diary'])

            st.write("### 🤖 AI Counsellor")

            st.markdown(
                f"<div class='ai-box'>{row['AI Response']}</div>",
                unsafe_allow_html=True
            )

else:
    st.info("No diary entries available yet.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <center>
        <h4>🌈 Student AI Diary Counsellor</h4>
        <p>
        Created to support students with emotional wellness,
        stress management, and self-expression.
        </p>
    </center>
    """,
    unsafe_allow_html=True
)