import streamlit as st
import random

st.set_page_config(
    page_title="Report Card Generator",
    page_icon="📘",
    layout="centered"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #2563eb);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #dbeafe;
    margin-bottom: 30px;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    border-radius: 12px;
}

.report-box {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.15);
    color: white;
    font-size: 18px;
    line-height: 1.7;
    margin-top: 20px;
}

.small-note {
    color: #dbeafe;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📘 Report Card App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Create positive, ESL-focused student reports in one click</div>', unsafe_allow_html=True)

# ---------- INPUTS ----------
with st.container():
    st.subheader("Student Details")

    student_name = st.text_input("Student Name")
    class_name = st.text_input("Class")
    age = st.number_input("Age", min_value=5, max_value=13, value=7)

    girl_toggle = st.toggle("Girl")
    gender = "girl" if girl_toggle else "boy"

    st.markdown('<div class="small-note">Toggle ON = girl, OFF = boy</div>', unsafe_allow_html=True)

# ---------- WORD BANKS ----------
pronouns = {
    "boy": {"subj": "He", "obj": "him", "poss": "his"},
    "girl": {"subj": "She", "obj": "her", "poss": "her"}
}

p = pronouns[gender]

opening_lines = [
    f"{student_name} has had a very positive term and has shown a lovely attitude in English class.",
    f"{student_name} is a cheerful and hardworking student who has made pleasing progress in English this term.",
    f"It has been a pleasure teaching {student_name} this term. {p['subj']} comes to class with a bright and positive attitude.",
    f"{student_name} is a kind and enthusiastic learner who continues to grow in confidence during English lessons."
]

strength_lines = [
    f"{p['subj']} listens carefully during class activities and tries hard to follow English instructions.",
    f"{p['subj']} shows good participation in class and enjoys joining in with speaking and vocabulary activities.",
    f"{p['subj']} is developing well in {p['poss']} English skills and often shows strong effort during lessons.",
    f"{p['subj']} works well during class tasks and is becoming more confident when using English.",
    f"{p['subj']} has shown a positive approach to classroom learning and responds well to teacher support."
]

social_lines = [
    f"{student_name} is polite and respectful in class and works well with classmates.",
    f"{p['subj']} gets along well with other students and helps create a positive classroom environment.",
    f"{p['subj']} is kind to others and shows good behaviour during classroom activities.",
    f"{student_name} interacts well with classmates and takes part happily in pair and group work."
]

improvement_lines = [
    f"Moving forward, {student_name} would benefit from continuing to build {p['poss']} confidence when speaking in full English sentences.",
    f"One area for further growth is for {student_name} to speak more loudly and confidently during class activities.",
    f"As {p['subj'].lower()} continues to improve, {student_name} can focus on using more complete English sentences during lessons.",
    f"To continue making progress, {student_name} should keep practising speaking with greater confidence and consistency."
]

closing_lines = [
    f"Overall, {student_name} should feel proud of the progress made this term, and I look forward to seeing {p['obj']} continue to improve.",
    f"Overall, {student_name} has had a successful term in English, and I am very pleased with {p['poss']} effort.",
    f"I am very happy with {student_name}'s progress in English and look forward to seeing even more growth next term.",
    f"{student_name} has worked well this term, and I am confident that {p['subj'].lower()} will continue to develop strongly in English."
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
            file_name=f"{student_name.replace(' ', '_').lower()}_report.txt",
            mime="text/plain"
        )
