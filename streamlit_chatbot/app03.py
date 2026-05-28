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

    .ai-box {
        background: linear-gradient(to right, #dfe9ff, #edf3ff);
        padding: 18px;
        border-radius: 15px;
        border-left: 6px solid #4c6ef5;
        margin-top: 15px;
        color: #222;
        font-size: 17px;
    }

    .mood-box {
        background: linear-gradient(to right, #fff0f6, #ffe3ec);
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        font-size: 20px;
        margin-bottom: 15px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# TITLE SECTION
# ---------------------------------------------------

st.markdown(
    "<div class='title'>📘 AI Student Diary Counsellor</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>A safe and supportive space for students to manage stress, emotions, and daily challenges.</div>",
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

st.sidebar.success("✨ Daily Motivation: Small progress is still progress.")

st.sidebar.info(
    """
    💡 Remember:
    
    - Drink enough water
    - Sleep properly
    - Take study breaks
    - Ask for help when needed
    - Your mental health matters
    """
)

# ---------------------------------------------------
# IMPROVED AI COUNSELLOR FUNCTION
# ---------------------------------------------------

def ai_counsellor_response(text, mood):

    text = text.lower()

    # STRESS / EXAMS
    if (
        "stress" in text
        or "exam" in text
        or "homework" in text
        or "assignment" in text
    ):

        return (
            "📚 It sounds like you are carrying a lot of academic pressure right now. "
            "Please remember that no exam or assignment can define your worth as a person. "
            "Try breaking your work into smaller tasks and focus on completing one step at a time. "
            "Taking short study breaks, drinking water, and getting enough sleep can improve concentration. "
            "You are doing better than you think, and every effort you make matters. 🌟"
        )

    # SADNESS
    elif (
        "sad" in text
        or "cry" in text
        or "depressed" in text
        or "upset" in text
    ):

        return (
            "💙 I am really sorry that you are feeling emotionally overwhelmed right now. "
            "Your feelings are important and deserve kindness, care, and understanding. "
            "Sometimes difficult emotions can make everything feel heavier, but remember that tough moments do not last forever. "
            "Please try to speak with someone you trust, even if it is just a small conversation. "
            "You deserve support, happiness, and peace of mind. "
            "Take things slowly today and be gentle with yourself. 🌈"
        )

    # ANXIETY
    elif (
        "anxiety" in text
        or "worried" in text
        or "panic" in text
        or "fear" in text
        or "nervous" in text
    ):

        return (
            "🌿 Anxiety can make your thoughts feel loud and overwhelming, but you are not alone in this experience. "
            "Try taking a few slow deep breaths and focus only on the present moment. "
            "You do not need to solve everything immediately. "
            "Listening to calming music, journaling your thoughts, or taking a short walk may help calm your mind. "
            "Remember: your mind deserves rest just as much as your body does. "
            "You are stronger than your anxious thoughts. 💚"
        )

    # LONELY
    elif "lonely" in text or "alone" in text:

        return (
            "🤝 Feeling lonely can hurt deeply, especially during stressful times. "
            "Please remember that your presence matters and you deserve meaningful support and friendship. "
            "Even small connections can help. "
            "You are not invisible, and there are people who care about you more than you realize. 🌟"
        )

    # TIRED
    elif (
        "tired" in text
        or "burnout" in text
        or "exhausted" in text
        or "drained" in text
    ):

        return (
            "😴 You sound mentally and emotionally exhausted right now. "
            "Rest is not laziness — it is an important part of healing and growth. "
            "Try to step away from stress for a little while and do something calming that you enjoy. "
            "You deserve rest and care too. 💛"
        )

    # RELATIONSHIPS
    elif (
        "friend" in text
        or "relationship" in text
        or "fight" in text
        or "argument" in text
    ):

        return (
            "💞 Relationship problems can feel emotionally painful and confusing. "
            "Healthy communication and honesty are important in every friendship and relationship. "
            "Remember to protect your own emotional wellbeing too. 🌸"
        )

    # LOW CONFIDENCE
    elif (
        "failure" in text
        or "useless" in text
        or "not good enough" in text
        or "hate myself" in text
    ):

        return (
            "🌟 Please do not define yourself by temporary setbacks. "
            "Every person experiences failure while growing and learning. "
            "Your value is not based on grades or other people's opinions. "
            "You are still improving every single day. 💖"
        )

    # HAPPY
    elif mood == "Happy 😊":

        return (
            "✨ It is wonderful to hear positive energy in your day today. "
            "Celebrate the small happy moments because they matter too. "
            "Keep appreciating your progress and continue spreading positivity. 🌈"
        )

    # DEFAULT
    else:

        return (
            "🌈 Thank you for sharing your thoughts and feelings today. "
            "Expressing emotions takes courage, and you should be proud of yourself for opening up. "
            "Take things one step at a time and continue being kind to yourself. 💙"
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

            st.markdown(
                f"<div class='ai-box'>{response}</div>",
                unsafe_allow_html=True
            )

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