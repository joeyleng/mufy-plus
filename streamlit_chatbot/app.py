
import streamlit as st
import pandas as pd
from datetime import datetime
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student AI Diary Counsellor",
    page_icon="📘",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("📘 Student AI Diary Counsellor")
st.write(
    "A safe place for students to share feelings, stress, and daily problems."
)

# -----------------------------
# CSV File
# -----------------------------
FILE_NAME = "diary_entries.csv"

# Create CSV if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Time", "Diary Entry", "AI Response"])
    df.to_csv(FILE_NAME, index=False)

# Load existing data
entries_df = pd.read_csv(FILE_NAME)

# -----------------------------
# AI Counsellor Function
# -----------------------------
def ai_counsellor_response(text):
    text = text.lower()

    if "stress" in text or "exam" in text:
        return (
            "It sounds like school pressure is affecting you. "
            "Try taking study breaks, sleeping well, and talking to someone you trust."
        )

    elif "sad" in text or "depressed" in text:
        return (
            "I am sorry you are feeling sad. Remember that your emotions matter "
            "and you do not need to handle everything alone."
        )

    elif "anxiety" in text or "worried" in text:
        return (
            "Feeling anxious can be difficult. Deep breathing, journaling, "
            "and focusing on one task at a time may help."
        )

    elif "tired" in text:
        return (
            "You may need some rest and self-care. "
            "Balancing studies with relaxation is important."
        )

    elif "lonely" in text:
        return (
            "Feeling lonely can be hard. Reaching out to friends, family, "
            "or support groups may help you feel more connected."
        )

    else:
        return (
            "Thank you for sharing your feelings today. "
            "Every step toward expressing yourself is important."
        )

# -----------------------------
# Diary Input
# -----------------------------
st.subheader("📝 Write About Your Day")

user_input = st.text_area(
    "How are you feeling today?",
    height=200,
    placeholder="Write your thoughts here..."
)

# -----------------------------
# Submit Button
# -----------------------------
if st.button("Submit Entry"):

    if user_input.strip() == "":
        st.warning("Please write something before submitting.")

    else:
        response = ai_counsellor_response(user_input)

        new_entry = {
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Diary Entry": user_input,
            "AI Response": response
        }

        # Add entry to dataframe
        entries_df = pd.concat(
            [entries_df, pd.DataFrame([new_entry])],
            ignore_index=True
        )

        # Save to CSV
        entries_df.to_csv(FILE_NAME, index=False)

        st.success("Your diary entry has been saved.")

        st.markdown("### 🤖 AI Counsellor")
        st.info(response)

# -----------------------------
# Display Previous Entries
# -----------------------------
st.subheader("📚 Previous Diary Entries")

if not entries_df.empty:

    # Show newest first
    reversed_df = entries_df.iloc[::-1]

    for _, row in reversed_df.iterrows():

        with st.expander(f"📅 {row['Time']}"):
            st.write("### 📝 Diary Entry")
            st.write(row["Diary Entry"])

            st.write("### 🤖 AI Counsellor Response")
            st.success(row["AI Response"])

else:
            st.write("No diary entries yet.")



