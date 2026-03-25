import streamlit as st
import random

st.set_page_config(
    page_title="Report Card Generator",
    page_icon="📘",
    layout="centered"
)

APP_PASSWORD = "Teachers1234"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔐 Please enter the password")
    entered_password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if entered_password.strip() == APP_PASSWORD:
            st.session_state.authenticated = True
            st.success("Access granted.")
            st.rerun()
        else:
            st.error("Wrong password.")

    st.stop()



# your app continues here


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

mode = st.selectbox(
    "Select Mode",
    ["Select One", "Single Report", "Bulk Report"]
)

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

strength_lines = [
    f"{p['subj']} listens carefully during lessons and follows instructions well. {p['subj']} is also becoming more confident when responding to familiar classroom English.",
    f"{p['subj']} shows a good understanding of classroom English and responds appropriately to tasks. {p['subj']} is developing confidence when using simple language during lessons.",
    f"{p['subj']} participates well in activities and is becoming more confident when using English. {p['subj']} continues to build a stronger understanding of key vocabulary.",
    f"{p['subj']} is developing a strong understanding of key vocabulary used in class. {p['subj']} is also improving in recognising and responding to familiar language.",
    f"{p['subj']} works hard during lessons and shows a positive effort in learning English. {p['subj']} is becoming more comfortable when following instructions independently.",
    f"{p['subj']} is making steady progress in understanding and using basic English expressions. {p['subj']} shows a growing ability to respond during classroom activities.",
    f"{p['subj']} shows good focus during class and is able to follow along with lesson activities. {p['subj']} is developing stronger listening and comprehension skills.",
    f"{p['subj']} is becoming more confident when responding to simple questions in English. {p['subj']} is also improving in understanding spoken instructions during lessons.",
    f"{p['subj']} demonstrates a growing ability to understand spoken English during class time. {p['subj']} is developing confidence when participating in guided activities.",
    f"{p['subj']} is developing well in recognising and using familiar English words. {p['subj']} continues to build confidence through consistent effort in class.",
    f"{p['subj']} shows a positive approach to learning new vocabulary and classroom language. {p['subj']} is beginning to use English more confidently during lessons.",
    f"{p['subj']} is building confidence in English and is beginning to use language more independently. {p['subj']} continues to improve through active participation in class.",
    f"{p['subj']} works well during guided activities and is improving in English step by step. {p['subj']} shows a good effort when completing classroom tasks.",
    f"{p['subj']} is showing encouraging progress in understanding instructions and classroom tasks. {p['subj']} is becoming more confident in responding during lessons.",
    f"{p['subj']} is developing stronger English skills through consistent effort in class. {p['subj']} continues to improve in both understanding and using language."

]

effort_lines = [
    f"{p['subj']} shows a consistent effort during English lessons and always tries to do {p['poss']} best. {p['subj']} approaches classroom tasks with a positive attitude.",
    f"{p['subj']} works hard during class activities and shows a willingness to improve. {p['subj']} continues to make a strong effort in English lessons.",
    f"{p['subj']} demonstrates a positive attitude toward learning and puts good effort into classwork. {p['subj']} is developing a strong learning routine.",
    f"{p['subj']} consistently shows effort during lessons and tries to complete tasks carefully. {p['subj']} is building good learning habits in English.",
    f"{p['subj']} puts a good amount of effort into classroom activities and shows a willingness to learn. {p['subj']} continues to improve through practice.",
    f"{p['subj']} shows strong effort in English lessons and approaches tasks with a positive mindset. {p['subj']} is developing confidence through hard work.",
    f"{p['subj']} works diligently during lessons and shows a positive learning attitude. {p['subj']} is continuing to improve through consistent effort.",
    f"{p['subj']} makes a good effort during English class and shows a willingness to participate. {p['subj']} is building stronger learning habits.",
    f"{p['subj']} demonstrates effort in all classroom activities and tries to improve each lesson. {p['subj']} shows a positive attitude toward learning.",
    f"{p['subj']} continues to show effort during lessons and approaches tasks with care. {p['subj']} is developing well through consistent practice."
]

participation_lines = [
    f"{p['subj']} participates actively during lessons and shows a willingness to try new activities. {p['subj']} is becoming more confident when taking part in class tasks.",
    f"{p['subj']} is becoming more confident when taking part in class activities. {p['subj']} shows a positive attitude toward participation during lessons.",
    f"{p['subj']} shows a positive attitude toward participation and is willing to join in activities. {p['subj']} is developing confidence when responding during class.",
    f"{p['subj']} responds well during class and makes a good effort to take part in activities. {p['subj']} is becoming more comfortable participating in lessons.",
    f"{p['subj']} is developing confidence when participating in English tasks and group work. {p['subj']} continues to improve through regular class involvement.",
    f"{p['subj']} takes part in lessons with encouragement and is building confidence over time. {p['subj']} shows a willingness to try during activities.",
    f"{p['subj']} is learning to participate more independently during classroom activities. {p['subj']} is showing steady improvement in class engagement.",
    f"{p['subj']} shows a growing willingness to answer questions and join class discussions. {p['subj']} is becoming more confident when participating.",
    f"{p['subj']} is making progress in participating during speaking and listening activities. {p['subj']} continues to show a positive effort in class.",
    f"{p['subj']} engages well in classroom tasks and shows interest in learning English. {p['subj']} is becoming more confident during lessons.",
    f"{p['subj']} participates with support and is gradually becoming more confident. {p['subj']} shows a positive approach to class activities.",
    f"{p['subj']} shows a cooperative attitude when taking part in classroom activities. {p['subj']} is developing confidence through regular participation.",
    f"{p['subj']} is beginning to take a more active role during lessons. {p['subj']} shows growing confidence when joining activities.",
    f"{p['subj']} responds positively during activities and shows a willingness to try. {p['subj']} is becoming more confident in participation.",
    f"{p['subj']} is developing confidence in joining group and pair work activities. {p['subj']} continues to improve through class involvement."

]

social_lines = [
    f"{student_name} is polite and respectful in class and works well with classmates. {p['subj']} contributes to a positive and friendly learning environment.",
    f"{p['subj']} gets along well with others and shows kindness during classroom activities. {p['subj']} helps create a supportive classroom atmosphere.",
    f"{p['subj']} demonstrates good behaviour and is a positive member of the class. {p['subj']} interacts well with classmates during activities.",
    f"{student_name} interacts well with classmates and contributes to a friendly classroom environment. {p['subj']} shows respect toward others during lessons.",
    f"{p['subj']} is cooperative and shows respect toward both teachers and classmates. {p['subj']} behaves well during classroom activities.",
    f"{p['subj']} behaves appropriately in class and helps maintain a positive learning atmosphere. {p['subj']} works well with others during group tasks.",
    f"{student_name} shows good manners and is considerate of others during lessons. {p['subj']} contributes to a calm and respectful classroom environment.",
    f"{p['subj']} works well in pairs and groups and shows a cooperative attitude. {p['subj']} interacts positively with classmates during activities.",
    f"{p['subj']} is kind to others and contributes to a supportive classroom environment. {p['subj']} shows respect during class interactions.",
    f"{student_name} continues to demonstrate positive classroom behaviour. {p['subj']} works well with classmates and follows expectations.",
    f"{p['subj']} is respectful during lessons and follows classroom expectations well. {p['subj']} contributes to a positive classroom environment.",
    f"{p['subj']} shows a calm and positive attitude when working with classmates. {p['subj']} behaves appropriately during group activities.",
    f"{student_name} behaves well in class and is a pleasure to teach. {p['subj']} interacts positively with others during lessons.",
    f"{p['subj']} is thoughtful toward others and works well in group settings. {p['subj']} shows good behaviour during class activities.",
    f"{p['subj']} contributes positively to the classroom and shows good social skills. {p['subj']} helps create a friendly and supportive environment."

]

improvement_lines = [
    f"Moving forward, {student_name} can continue to build confidence when speaking in full English sentences. With regular practice, {p['subj'].lower()} will become more comfortable expressing ideas clearly.",
    f"One area for further growth is developing greater confidence when answering in English. With continued encouragement, {p['subj'].lower()} will be able to respond more independently.",
    f"To continue improving, {student_name} would benefit from speaking more often during class activities. This will help {p['obj']} build confidence and fluency over time.",
    f"The next step for {student_name} is to continue building confidence when using English independently. With practice, {p['subj'].lower()} will become more comfortable using complete sentences.",
    f"With continued practice, {student_name} can develop greater confidence in speaking during lessons. This will support stronger communication skills in English.",
    f"{student_name} would benefit from continuing to use fuller English sentences when responding in class. With support, {p['subj'].lower()} will continue to improve steadily.",
    f"An important goal for {student_name} is to become more confident when expressing ideas in English. With practice, {p['subj'].lower()} will be able to speak more clearly and independently.",
    f"As {p['subj'].lower()} continues to progress, {student_name} can focus on speaking more clearly and confidently in class. This will help strengthen overall English communication skills.",
    f"With encouragement and practice, {student_name} can continue to strengthen speaking confidence in English lessons. This will allow {p['obj']} to participate more actively.",
    f"To make further progress, {student_name} can focus on answering questions with greater confidence and detail. With time, {p['subj'].lower()} will improve in this area.",
    f"{student_name} is ready to take the next step by continuing to build confidence in spoken English. With practice, {p['subj'].lower()} will become more independent when speaking.",
    f"Going forward, {student_name} can continue improving by using English more independently during class. This will support continued progress in communication skills.",
    f"One helpful area to focus on is speaking with more confidence during classroom activities. With regular practice, {p['subj'].lower()} will continue to improve.",
    f"As confidence grows, {student_name} can continue working on answering in more complete English sentences. This will help build stronger communication skills.",
    f"With steady practice, {student_name} can continue to develop stronger confidence when speaking English. This will support continued growth in English learning."

]

closing_lines = [
    f"Overall, {student_name} has made positive progress in English this term. {p['subj']} should feel proud of the effort shown during lessons.",
    f"I am very pleased with {student_name}'s progress in English this term. {p['subj']} has shown a positive attitude toward learning.",
    f"{student_name} has worked well in English this term and continues to improve. {p['subj']} should be proud of this progress.",
    f"Overall, {student_name} has shown encouraging development in English. {p['subj']} continues to build confidence in class.",
    f"I am happy with {student_name}'s effort and progress in English lessons. {p['subj']} is continuing to improve steadily.",
    f"{student_name} has demonstrated a positive approach to learning English this term. {p['subj']} is making steady progress.",
    f"Overall, {student_name} has done well in English and continues to grow. {p['subj']} shows a positive attitude toward learning.",
    f"I am pleased with the progress {student_name} has made in English this term. {p['subj']} continues to develop confidence.",
    f"{student_name} has made good progress in English and shows a strong effort. {p['subj']} is continuing to improve.",
    f"Overall, {student_name} has shown a positive attitude and steady progress in English. {p['subj']} continues to develop skills.",
    f"{student_name} has worked hard this term and has made encouraging progress in English. {p['subj']} should feel proud.",
    f"I am very satisfied with {student_name}'s progress in English lessons. {p['subj']} continues to show a positive approach.",
    f"{student_name} continues to make steady progress in English and shows good effort. {p['subj']} is developing confidence.",
    f"Overall, {student_name} has had a successful term in English. {p['subj']} continues to improve in a positive way.",
    f"{student_name} has shown good effort and progress in English this term. {p['subj']} is continuing to grow in confidence."

]

def generate_report(name, pronouns):
    student_name = name
    p = pronouns

    report = " ".join([
        random.choice(opening_lines),
        random.choice(strength_lines),
        random.choice(effort_lines),
        random.choice(participation_lines),
        random.choice(social_lines),
        random.choice(improvement_lines),
        f"{student_name}, keep up the hard work."
    ])

    return report
    
# ---------- SINGLE REPORT ----------
if mode == "Single Report":
    if st.button("✨ Generate Report Card"):
        if not student_name.strip():
            st.warning("Please enter the student's name.")
        else:
            report = generate_report(student_name, p)

            st.subheader("Generated Report")
            st.markdown(
                f'<div class="report-box">{report}</div>',
                unsafe_allow_html=True
            )

            word_count = len(report.split())
            st.write(f"Word count: {word_count}")

            st.download_button(
                "📥 Download Report",
                report,
                file_name=f"{student_name}_report.txt"
            )

# ---------- BULK REPORT ----------
if mode == "Bulk Report":
    st.markdown("---")
    st.subheader("📚 Bulk Report Generator")
    st.write("Enter one student per line in this format: Name,g or Name,b")

    bulk_names = st.text_area(
        "Bulk Student List",
        height=220,
        placeholder="Yuha,g\nBonnie,g\nHyun,b\nLiam,b"
    )

    if st.button("✨ Generate Bulk Reports"):
        lines = [line.strip() for line in bulk_names.splitlines() if line.strip()]

        if not lines:
            st.warning("Please enter at least one student.")
        else:
            all_reports_text = ""

            for line in lines:
                parts = [part.strip() for part in line.split(",")]

                if len(parts) != 2:
                    st.error(f"Wrong format: {line}")
                    continue

                name, gender_code = parts

                if gender_code.lower() == "b":
                    bulk_p = {"subj": "He", "obj": "him", "poss": "his"}
                elif gender_code.lower() == "g":
                    bulk_p = {"subj": "She", "obj": "her", "poss": "her"}
                else:
                    st.error(f"Gender must be b or g: {line}")
                    continue

                report = generate_report(name, bulk_p)
                word_count = len(report.split())

                st.markdown(f"### {name}")
                st.markdown(
                    f'<div class="report-box">{report}</div>',
                    unsafe_allow_html=True
                )
                st.write(f"Word count: {word_count}")

                all_reports_text += (
                    f"{name}\n"
                    f"{report}\n"
                    f"Word count: {word_count}\n"
                    f"{'-'*50}\n\n"
                )

            if all_reports_text:
                st.download_button(
                    "📥 Download All Bulk Reports",
                    all_reports_text,
                    file_name="bulk_reports.txt",
                    mime="text/plain"
                )
