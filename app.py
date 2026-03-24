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
    background-color: #0f172a;
    color: #ffffff !important;
    font-weight: bold;
}

label, p, div, span {
    color: #ffffff !important;
    font-weight: bold !important;
}

input, textarea {
    color: #ffffff !important;
    background-color: #1e293b !important;
    border-radius: 10px !important;
    border: 1px solid #334155 !important;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    color: #ffffff;
}

.sub-title {
    text-align: center;
    font-size: 16px;
    color: #e2e8f0;
    font-weight: bold;
}

.report-box {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #334155;
    font-size: 17px;
    line-height: 1.8;
    margin-top: 20px;
    color: #ffffff;
    font-weight: bold;
}

button {
    font-weight: bold !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="main-title">📘 Report Card Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Create positive ESL student reports in one click</div>', unsafe_allow_html=True)

# ---------- INPUTS ----------
st.subheader("Student infomation ")

student_name = st.text_input("Student Name")
class_name = st.text_input("Class")
age = st.number_input("Age", min_value=5, max_value=13, value=7)
gender = st.radio("Select Gender", ["Boy", "Girl"])

# ---------- PRONOUNS ----------
if gender == "Boy":
    p = {"subj": "He", "obj": "him", "poss": "his"}
else:
    p = {"subj": "She", "obj": "her", "poss": "her"}

# ---------- SENTENCE BANKS ----------
opening_lines = [
    f"{student_name} has had a very positive term in English and has shown a cheerful attitude toward learning.",
    f"It has been a pleasure teaching {student_name} this term in English.",
    f"{student_name} is a motivated student who continues to make steady progress in English lessons.",
    f"Throughout the term, {student_name} has shown a positive approach to English class.",
    f"{student_name} has worked hard in English this term and should feel proud of this progress.",
    f"{student_name} is a bright and enthusiastic student who enjoys participating in English activities.",
    f"{student_name} has shown a consistent effort in English and continues to develop important language skills.",
    f"In English class, {student_name} has demonstrated a positive attitude and a willingness to learn.",
    f"{student_name} has made encouraging progress in English and approaches lessons with a good mindset.",
    f"{student_name} is developing well in English and continues to grow in confidence each week.",
    f"{student_name} has shown great effort during English lessons and is building a strong foundation.",
    f"{student_name} continues to approach English learning with energy and a positive attitude.",
    f"{student_name} has shown pleasing progress in English and is becoming more confident in class.",
    f"{student_name} is a hardworking student who is steadily improving in English lessons.",
    f"{student_name} has had a successful term in English and continues to show a strong effort in class."
]

strength_lines = [
    f"{p['subj']} listens carefully during lessons and follows instructions well.",
    f"{p['subj']} shows a good understanding of classroom English and responds appropriately to tasks.",
    f"{p['subj']} participates well in activities and is becoming more confident when using English.",
    f"{p['subj']} is developing a strong understanding of key vocabulary used in class.",
    f"{p['subj']} works hard during lessons and shows a positive effort in learning English.",
    f"{p['subj']} is making steady progress in understanding and using basic English expressions.",
    f"{p['subj']} shows good focus during class and is able to follow along with lesson activities.",
    f"{p['subj']} is becoming more confident when responding to simple questions in English.",
    f"{p['subj']} demonstrates a growing ability to understand spoken English during class time.",
    f"{p['subj']} is developing well in recognising and using familiar English words.",
    f"{p['subj']} shows a positive approach to learning new vocabulary and classroom language.",
    f"{p['subj']} is building confidence in English and is beginning to use language more independently.",
    f"{p['subj']} works well during guided activities and is improving in English step by step.",
    f"{p['subj']} is showing encouraging progress in understanding instructions and classroom tasks.",
    f"{p['subj']} is developing stronger English skills through consistent effort in class."
]

participation_lines = [
    f"During class, {student_name} usually participates well and shows a positive willingness to join in learning activities. {p['subj']} responds well during speaking practice, vocabulary review, and simple question-and-answer tasks. Even when {p['subj'].lower()} feels unsure, {p['subj'].lower()} still tries to take part, which is very pleasing to see.",
    
    f"{student_name} has made encouraging progress in classroom participation. {p['subj']} is becoming more willing to answer questions, repeat target language, and engage in activities with teacher support. {p['subj']} often tries hard during lessons and shows that {p['subj'].lower()} wants to improve.",
    
    f"{p['subj']} takes part well in class activities and usually shows a cooperative attitude toward learning. {student_name} is especially developing confidence during guided practice and small classroom tasks. {p['subj']} is learning to take a more active role in lessons, which is helping {p['obj']} continue to grow."
]

social_lines = [
    f"{student_name} is also a polite and respectful member of the classroom. {p['subj']} works well with classmates and shows kindness during pair and group activities. {p['subj']} contributes to a pleasant classroom atmosphere and generally demonstrates good manners during lessons.",
    
    f"In addition, {student_name} interacts well with other students and shows respectful behaviour in class. {p['subj']} is able to work cooperatively with classmates and usually approaches group tasks with a calm and positive attitude. This helps create a supportive learning environment for everyone.",
    
    f"{student_name} continues to show positive classroom behaviour and gets along well with others. {p['subj']} is courteous, cooperative, and able to participate appropriately during class activities. {p['subj']} helps maintain a comfortable and friendly learning environment."
]

improvement_lines = [
    f"Moving forward, one important area for further growth will be continuing to build confidence when speaking in full English sentences. As {student_name} becomes more comfortable using English, {p['subj'].lower()} will benefit from taking a little more time to respond verbally with complete answers. With regular practice and continued encouragement, I am confident that {p['subj'].lower()} will keep improving in this area.",
    
    f"To continue making progress, {student_name} would benefit from developing greater confidence when speaking English more independently. {p['subj']} already shows a good understanding of classroom language, and the next step will be to express ideas more clearly using fuller spoken responses. With more practice, {p['subj'].lower()} is likely to become an even more confident English speaker.",
    
    f"One area to focus on next term is speaking with greater confidence and consistency during English activities. {student_name} is capable of participating well, and with continued support, {p['subj'].lower()} can continue to strengthen {p['poss']} ability to answer using more complete English sentences. This will help {p['obj']} build even stronger communication skills."
]

closing_lines = [
    f"Overall, {student_name} has had a successful term in English and should feel proud of the progress made so far. {p['subj']} has shown a positive attitude, a willingness to learn, and a steady effort throughout lessons. I am very pleased with {p['poss']} development and look forward to seeing {p['obj']} continue to grow next term.",
    
    f"Overall, I am very happy with {student_name}'s progress in English this term. {p['subj']} has worked hard, shown a pleasing attitude toward learning, and continued to build important skills in class. I look forward to seeing even more growth and confidence from {p['obj']} in the future.",
    
    f"In summary, {student_name} has made encouraging progress and has contributed positively to English class this term. {p['subj']} has shown good effort, developing confidence, and a respectful attitude toward learning. I am pleased with {p['poss']} progress and look forward to seeing continued success in the future."
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
        word_count = len(report.split())
        st.write(f"Word count: {word_count}")

        st.download_button(
            "📥 Download Report",
            report,
            file_name=f"{student_name}_report.txt"
        )
