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

mode = st.selectbox(
    "Select Mode",
    ["Select One", "Single Report", "Bulk Report"]
)

# ---------- SENTENCE BANKS ----------
opening_lines = [
    "{student_name} has had a very positive term in English and has shown a cheerful attitude toward learning. {subj} comes to class ready to participate and responds well to teacher guidance.",
    "It has been a pleasure teaching {student_name} this term in English. {subj} shows a positive mindset during lessons and is developing confidence in a steady way.",
    "{student_name} is a motivated student who continues to make steady progress in English lessons. {subj} approaches activities with a good attitude and a willingness to learn.",
    "Throughout the term, {student_name} has shown a positive approach to English class. {subj} is becoming more comfortable with classroom routines and expectations.",
    "{student_name} has worked hard in English this term and should feel proud of this progress. {subj} shows a consistent effort during lessons and responds well to support.",
    "{student_name} is a bright and enthusiastic student who enjoys participating in English activities. {subj} shows interest in learning and continues to build confidence each week.",
    "{student_name} has shown a consistent effort in English and continues to develop important language skills. {subj} approaches tasks with a positive attitude and tries to do {poss} best.",
    "In English class, {student_name} has demonstrated a positive attitude and a willingness to learn. {subj} listens carefully and is developing stronger classroom confidence.",
    "{student_name} has made encouraging progress in English and approaches lessons with a good mindset. {subj} is becoming more confident when participating in class activities.",
    "{student_name} is developing well in English and continues to grow in confidence each week. {subj} shows a positive attitude and responds well to classroom instruction.",
    "{student_name} has shown great effort during English lessons and is building a strong foundation. {subj} is developing confidence and becoming more comfortable using English.",
    "{student_name} continues to approach English learning with energy and a positive attitude. {subj} is making steady progress and showing a willingness to improve.",
    "{student_name} has shown pleasing progress in English and is becoming more confident in class. {subj} participates with encouragement and shows a positive learning attitude.",
    "{student_name} is a hardworking student who is steadily improving in English lessons. {subj} shows a good understanding of classroom expectations and routines.",
    "{student_name} has had a successful term in English and continues to show a strong effort in class. {subj} is developing confidence and responding well during lessons."
]

strength_lines = [
    "{subj} listens carefully during lessons and follows instructions well. {subj} is also becoming more confident when responding to familiar classroom English.",
    "{subj} shows a good understanding of classroom English and responds appropriately to tasks. {subj} is developing confidence when using simple language during lessons.",
    "{subj} participates well in activities and is becoming more confident when using English. {subj} continues to build a stronger understanding of key vocabulary.",
    "{subj} is developing a strong understanding of key vocabulary used in class. {subj} is also improving in recognising and responding to familiar language.",
    "{subj} works hard during lessons and shows a positive effort in learning English. {subj} is becoming more comfortable when following instructions independently.",
    "{subj} is making steady progress in understanding and using basic English expressions. {subj} shows a growing ability to respond during classroom activities.",
    "{subj} shows good focus during class and is able to follow along with lesson activities. {subj} is developing stronger listening and comprehension skills.",
    "{subj} is becoming more confident when responding to simple questions in English. {subj} is also improving in understanding spoken instructions during lessons.",
    "{subj} demonstrates a growing ability to understand spoken English during class time. {subj} is developing confidence when participating in guided activities.",
    "{subj} is developing well in recognising and using familiar English words. {subj} continues to build confidence through consistent effort in class.",
    "{subj} shows a positive approach to learning new vocabulary and classroom language. {subj} is beginning to use English more confidently during lessons.",
    "{subj} is building confidence in English and is beginning to use language more independently. {subj} continues to improve through active participation in class.",
    "{subj} works well during guided activities and is improving in English step by step. {subj} shows a good effort when completing classroom tasks.",
    "{subj} is showing encouraging progress in understanding instructions and classroom tasks. {subj} is becoming more confident in responding during lessons.",
    "{subj} is developing stronger English skills through consistent effort in class. {subj} continues to improve in both understanding and using language."

]

effort_lines = [
    "{subj} shows a consistent effort during English lessons and always tries to do {poss} best. {subj} approaches classroom tasks with a positive attitude.",
    "{subj} works hard during class activities and shows a willingness to improve. {subj} continues to make a strong effort in English lessons.",
    "{subj} demonstrates a positive attitude toward learning and puts good effort into classwork. {subj} is developing a strong learning routine.",
    "{subj} consistently shows effort during lessons and tries to complete tasks carefully. {subj} is building good learning habits in English.",
    "{subj} puts a good amount of effort into classroom activities and shows a willingness to learn. {subj} continues to improve through practice.",
    "{subj} shows strong effort in English lessons and approaches tasks with a positive mindset. {subj} is developing confidence through hard work.",
    "{subj} works diligently during lessons and shows a positive learning attitude. {subj} is continuing to improve through consistent effort.",
    "{subj} makes a good effort during English class and shows a willingness to participate. {subj} is building stronger learning habits.",
    "{subj} demonstrates effort in all classroom activities and tries to improve each lesson. {subj} shows a positive attitude toward learning.",
    "{subj} continues to show effort during lessons and approaches tasks with care. {subj} is developing well through consistent practice."

]

participation_lines = [
    "{subj} participates actively during lessons and shows a willingness to try new activities. {subj} is becoming more confident when taking part in class tasks.",
    "{subj} is becoming more confident when taking part in class activities. {subj} shows a positive attitude toward participation during lessons.",
    "{subj} shows a positive attitude toward participation and is willing to join in activities. {subj} is developing confidence when responding during class.",
    "{subj} responds well during class and makes a good effort to take part in activities. {subj} is becoming more comfortable participating in lessons.",
    "{subj} is developing confidence when participating in English tasks and group work. {subj} continues to improve through regular class involvement.",
    "{subj} takes part in lessons with encouragement and is building confidence over time. {subj} shows a willingness to try during activities.",
    "{subj} is learning to participate more independently during classroom activities. {subj} is showing steady improvement in class engagement.",
    "{subj} shows a growing willingness to answer questions and join class discussions. {subj} is becoming more confident when participating.",
    "{subj} is making progress in participating during speaking and listening activities. {subj} continues to show a positive effort in class.",
    "{subj} engages well in classroom tasks and shows interest in learning English. {subj} is becoming more confident during lessons.",
    "{subj} participates with support and is gradually becoming more confident. {subj} shows a positive approach to class activities.",
    "{subj} shows a cooperative attitude when taking part in classroom activities. {subj} is developing confidence through regular participation.",
    "{subj} is beginning to take a more active role during lessons. {subj} shows growing confidence when joining activities.",
    "{subj} responds positively during activities and shows a willingness to try. {subj} is becoming more confident in participation.",
    "{subj} is developing confidence in joining group and pair work activities. {subj} continues to improve through class involvement."

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
    "Moving forward, {student_name} can continue to build confidence when speaking in full English sentences. With regular practice, {subj_l} will become more comfortable expressing ideas clearly.",
    "One area for further growth is developing greater confidence when answering in English. With continued encouragement, {subj_l} will be able to respond more independently.",
    "To continue improving, {student_name} would benefit from speaking more often during class activities. This will help {obj} build confidence and fluency over time.",
    "The next step for {student_name} is to continue building confidence when using English independently. With practice, {subj_l} will become more comfortable using complete sentences.",
    "With continued practice, {student_name} can develop greater confidence in speaking during lessons. This will support stronger communication skills in English.",
    "{student_name} would benefit from continuing to use fuller English sentences when responding in class. With support, {subj_l} will continue to improve steadily.",
    "An important goal for {student_name} is to become more confident when expressing ideas in English. With practice, {subj_l} will be able to speak more clearly and independently.",
    "As {subj_l} continues to progress, {student_name} can focus on speaking more clearly and confidently in class. This will help strengthen overall English communication skills.",
    "With encouragement and practice, {student_name} can continue to strengthen speaking confidence in English lessons. This will allow {obj} to participate more actively.",
    "To make further progress, {student_name} can focus on answering questions with greater confidence and detail. With time, {subj_l} will improve in this area.",
    "{student_name} is ready to take the next step by continuing to build confidence in spoken English. With practice, {subj_l} will become more independent when speaking.",
    "Going forward, {student_name} can continue improving by using English more independently during class. This will support continued progress in communication skills.",
    "One helpful area to focus on is speaking with more confidence during classroom activities. With regular practice, {subj_l} will continue to improve.",
    "As confidence grows, {student_name} can continue working on answering in more complete English sentences. This will help build stronger communication skills.",
    "With steady practice, {student_name} can continue to develop stronger confidence when speaking English. This will support continued growth in English learning."
]

closing_lines = [
    "Overall, {student_name} has made positive progress in English this term. {subj} should feel proud of the effort shown during lessons.",
    "I am very pleased with {student_name}'s progress in English this term. {subj} has shown a positive attitude toward learning.",
    "{student_name} has worked well in English this term and continues to improve. {subj} should be proud of this progress.",
    "Overall, {student_name} has shown encouraging development in English. {subj} continues to build confidence in class.",
    "I am happy with {student_name}'s effort and progress in English lessons. {subj} is continuing to improve steadily.",
    "{student_name} has demonstrated a positive approach to learning English this term. {subj} is making steady progress.",
    "Overall, {student_name} has done well in English and continues to grow. {subj} shows a positive attitude toward learning.",
    "I am pleased with the progress {student_name} has made in English this term. {subj} continues to develop confidence.",
    "{student_name} has made good progress in English and shows a strong effort. {subj} is continuing to improve.",
    "Overall, {student_name} has shown a positive attitude and steady progress in English. {subj} continues to develop skills.",
    "{student_name} has worked hard this term and has made encouraging progress in English. {subj} should feel proud.",
    "I am very satisfied with {student_name}'s progress in English lessons. {subj} continues to show a positive approach.",
    "{student_name} continues to make steady progress in English and shows good effort. {subj} is developing confidence.",
    "Overall, {student_name} has had a successful term in English. {subj} continues to improve in a positive way.",
    "{student_name} has shown good effort and progress in English this term. {subj} is continuing to grow in confidence."

]

def generate_report(name, pronouns):
    student_name = name

    report = " ".join([
    random.choice(opening_lines),
    random.choice(strength_lines),
    random.choice(effort_lines),
    random.choice(participation_lines),
    random.choice(social_lines),
    random.choice(improvement_lines),
    random.choice(closing_lines),  # 👈 NEW
    "{student_name}, keep up the hard work."])

    report = report.format(
        student_name=student_name,
        subj=pronouns["subj"],
        obj=pronouns["obj"],
        poss=pronouns["poss"]
    )

    return report
    
mode = st.selectbox(
    "Select Mode",
    ["Select One", "Single Report", "Bulk Report"]
)

# ---------- SINGLE REPORT ----------
if mode == "Single Report":
    st.subheader("Student information")

    student_name = st.text_input("Student Name")
    class_name = st.text_input("Class")
    age = st.number_input("Age", min_value=5, max_value=13, value=7)
    gender = st.radio("Select Gender", ["Boy", "Girl"])

    if gender == "Boy":
        p = {"subj": "He", "obj": "him", "poss": "his"}
    else:
        p = {"subj": "She", "obj": "her", "poss": "her"}

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
elif mode == "Bulk Report":
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
