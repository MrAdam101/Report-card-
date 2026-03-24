import streamlit as st
import random

st.set_page_config(
    page_title="Report Card Generator",
    page_icon="📘",
    layout="centered"
)

# ---------- CLEAN STYLE ----------
st.markdown("""
<style>
.stApp {
    background-color: #ffffff;
    color: #1e293b;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    font-size: 16px;
    color: #475569;
    margin-bottom: 30px;
}

.report-box {
    background: #f1f5f9;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    font-size: 17px;
    line-height: 1.7;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="main-title">📘 Report Card App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Create positive, ESL-focused student reports in one click</div>', unsafe_allow_html=True)

# ---------- INPUTS ----------
st.subheader("Student Details")

student_name = st.text_input("Student Name")
class_name = st.text_input("Class")
age = st.number_input("Age", min_value=5, max_value=13, value=7)

# FIXED GENDER SELECT
gender = st.radio("Select Gender", ["Boy", "Girl"])

# ---------- PRONOUNS ----------
if gender == "Boy":
    p = {"subj": "He", "obj": "him", "poss": "his"}
else:
    p = {"subj": "She", "obj": "her", "poss": "her"}

# ---------- SENTENCE BANK ----------
opening_lines = [
    f"{student_name} has had a very positive term and shows a great attitude in English class.",
    f"{student_name} is a cheerful and hardworking student who is making steady progress in English.",
    f"It has been a pleasure teaching {student_name}. {p['subj']} comes to class with a positive mindset.",
]

strength_lines = [
    f"{p['subj']} listens carefully and follows instructions well.",
    f"{p['subj']} participates actively in class and enjoys learning new words.",
    f"{p['subj']} is building strong English skills and shows great effort.",
]

social_lines = [
    f"{student_name} is polite and works well with classmates.",
    f"{p['subj']} is kind to others and contributes to a positive classroom.",
]

improvement_lines = [
    f"Moving forward, {student_name} can improve by speaking more confidently in full sentences.",
    f"One area to develop is increasing confidence when speaking English.",
]

closing_lines = [
    f"Overall, {student_name} has done well this term and should feel proud.",
    f"I am very happy with {student_name}'s progress and look forward to continued improvement.",
]

# ---------- GENERATE ----------
if st.button("✨ Generate Report Card"):
    if not student_name.strip():
        st.warning("Please enter the student's name.")
    else:
        report = " ".join([
            random.choice(opening_lines),
            random.choice(strength_lines),
            random.choice(social_lines),
            random.choice(improvement_lines),
            random.choice(closing_lines)
        ])

        st.subheader("Generated Report")
        st.markdown(f'<div class="report-box">{report}</div>', unsafe_allow_html=True)

        st.download_button(
            "📥 Download Report",
            report,
            file_name=f"{student_name}_report.txt"
        )
