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
    f"{student_name} has had a very positive term in English and has shown a cheerful attitude toward learning. {p['subj']} comes to class ready to participate and responds well to teacher guidance.",
    
    f"It has been a pleasure teaching {student_name} this term in English. {p['subj']} shows a positive mindset during lessons and is developing confidence in a steady way.",
    
    f"{student_name} is a motivated student who continues to make steady progress in English lessons. {p['subj']} approaches activities with a good attitude and a willingness to learn.",
    
    f"Throughout the term, {student_name} has shown a positive approach to English class. {p['subj']} is becoming more comfortable with classroom routines and expectations.",
    
    f"{student_name} has worked hard in English this term and should feel proud of this progress. {p['subj']} shows a consistent effort during lessons and responds well to support.",
    
    f"{student_name} is a bright and enthusiastic student who enjoys participating in English activities. {p['subj']} shows interest in learning and continues to build confidence each week.",
    
    f"{student_name} has shown a consistent effort in English and continues to develop important language skills. {p['subj']} approaches tasks with a positive attitude and tries to do {p['poss']} best.",
    
    f"In English class, {student_name} has demonstrated a positive attitude and a willingness to learn. {p['subj']} listens carefully and is developing stronger classroom confidence.",
    
    f"{student_name} has made encouraging progress in English and approaches lessons with a good mindset. {p['subj']} is becoming more confident when participating in class activities.",
    
    f"{student_name} is developing well in English and continues to grow in confidence each week. {p['subj']} shows a positive attitude and responds well to classroom instruction.",
    
    f"{student_name} has shown great effort during English lessons and is building a strong foundation. {p['subj']} is developing confidence and becoming more comfortable using English.",
    
    f"{student_name} continues to approach English learning with energy and a positive attitude. {p['subj']} is making steady progress and showing a willingness to improve.",
    
    f"{student_name} has shown pleasing progress in English and is becoming more confident in class. {p['subj']} participates with encouragement and shows a positive learning attitude.",
    
    f"{student_name} is a hardworking student who is steadily improving in English lessons. {p['subj']} shows a good understanding of classroom expectations and routines.",
    
    f"{student_name} has had a successful term in English and continues to show a strong effort in class. {p['subj']} is developing confidence and responding well during lessons."
]
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
    f"{p['subj']} participates actively during lessons and shows a willingness to try new activities.",
    f"{p['subj']} is becoming more confident when taking part in class activities.",
    f"{p['subj']} shows a positive attitude toward participation and is willing to join in.",
    f"{p['subj']} responds well during class and makes a good effort to take part in activities.",
    f"{p['subj']} is developing confidence when participating in English tasks and group work.",
    f"{p['subj']} takes part in lessons with encouragement and is building confidence over time.",
    f"{p['subj']} is learning to participate more independently during classroom activities.",
    f"{p['subj']} shows a growing willingness to answer questions and join class discussions.",
    f"{p['subj']} is making progress in participating during speaking and listening activities.",
    f"{p['subj']} engages well in classroom tasks and shows interest in learning English.",
    f"{p['subj']} participates with support and is gradually becoming more confident.",
    f"{p['subj']} shows a cooperative attitude when taking part in classroom activities.",
    f"{p['subj']} is beginning to take a more active role during lessons.",
    f"{p['subj']} responds positively during activities and shows a willingness to try.",
    f"{p['subj']} is developing confidence in joining group and pair work activities."
]

social_lines = [
    f"{student_name} is polite and respectful in class and works well with classmates.",
    f"{p['subj']} gets along well with others and shows kindness during classroom activities.",
    f"{p['subj']} demonstrates good behaviour and is a positive member of the class.",
    f"{student_name} interacts well with classmates and contributes to a friendly classroom environment.",
    f"{p['subj']} is cooperative and shows respect toward both teachers and classmates.",
    f"{p['subj']} behaves appropriately in class and helps maintain a positive learning atmosphere.",
    f"{student_name} shows good manners and is considerate of others during lessons.",
    f"{p['subj']} works well in pairs and groups and shows a cooperative attitude.",
    f"{p['subj']} is kind to others and contributes to a supportive classroom environment.",
    f"{student_name} continues to demonstrate positive classroom behaviour.",
    f"{p['subj']} is respectful during lessons and follows classroom expectations well.",
    f"{p['subj']} shows a calm and positive attitude when working with classmates.",
    f"{student_name} behaves well in class and is a pleasure to teach.",
    f"{p['subj']} is thoughtful toward others and works well in group settings.",
    f"{p['subj']} contributes positively to the classroom and shows good social skills."
]
improvement_lines = [
    f"Moving forward, {student_name} can continue to build confidence when speaking in full English sentences.",
    f"One area for further growth is developing greater confidence when answering in English.",
    f"To continue improving, {student_name} would benefit from speaking more often during class activities.",
    f"The next step for {student_name} is to continue building confidence when using English independently.",
    f"With continued practice, {student_name} can develop greater confidence in speaking during lessons.",
    f"{student_name} would benefit from continuing to use fuller English sentences when responding in class.",
    f"An important goal for {student_name} is to become more confident when expressing ideas in English.",
    f"As {p['subj'].lower()} continues to progress, {student_name} can focus on speaking more clearly and confidently in class.",
    f"With encouragement and practice, {student_name} can continue to strengthen speaking confidence in English lessons.",
    f"To make further progress, {student_name} can focus on answering questions with greater confidence and detail.",
    f"{student_name} is ready to take the next step by continuing to build confidence in spoken English.",
    f"Going forward, {student_name} can continue improving by using English more independently during class.",
    f"One helpful area to focus on is speaking with more confidence during classroom activities.",
    f"As confidence grows, {student_name} can continue working on answering in more complete English sentences.",
    f"With steady practice, {student_name} can continue to develop stronger confidence when speaking English."
]

closing_lines = [
    f"I am very pleased with {student_name}'s progress this term.",
    f"Overall, {student_name} has done very well in English this term.",
    f"{student_name} should feel proud of the progress made in English.",
    f"I look forward to seeing {student_name} continue to improve next term.",
    f"{student_name} has shown great effort and should be proud of this progress."
]
# ---------- GENERATE ----------
# ---------- GENERATE ----------
if st.button("✨ Generate Report Card"):
    if not student_name.strip():
        st.warning("Please enter the student's name.")
    else:
        report = " ".join([
           random.choice(opening_lines),
           random.choice(strength_lines),
           random.choice(participation_lines),
           random.choice(social_lines),
           random.choice(improvement_lines),
           f"{student_name}, keep up the hard work."
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
          
