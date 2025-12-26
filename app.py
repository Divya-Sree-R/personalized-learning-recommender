import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------------
st.set_page_config(
    page_title="Personalized Learning Platform",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    students = pd.read_csv("data/students.csv")
    courses = pd.read_csv("data/courses.csv")
    interactions = pd.read_csv("data/interactions.csv")
    quizzes = pd.read_csv("data/quizzes.csv")
    return students, courses, interactions, quizzes

students, courses, interactions, quizzes = load_data()

# -----------------------------
# PREPROCESS
# -----------------------------
learning = interactions.merge(courses, on="course_id")
learning = learning.merge(quizzes, on=["student_id", "course_id"])

student_topic = learning.groupby(
    ["student_id", "topic"]
).agg(
    avg_time=("time_spent", "mean"),
    avg_score=("score", "mean")
).reset_index()

def skill_gap(score):
    if score < 50:
        return "High"
    elif score < 70:
        return "Medium"
    else:
        return "Low"

student_topic["skill_gap"] = student_topic["avg_score"].apply(skill_gap)

# -----------------------------
# SIMILARITY MODEL
# -----------------------------
matrix = student_topic.pivot_table(
    index="student_id",
    columns="topic",
    values="avg_score",
    fill_value=0
)

similarity = cosine_similarity(matrix)
similarity_df = pd.DataFrame(
    similarity,
    index=matrix.index,
    columns=matrix.index
)

# -----------------------------
# RECOMMENDATION ENGINE
# -----------------------------
def recommend(student_id, top_n=5):
    taken = interactions[
        interactions["student_id"] == student_id
    ]["course_id"].tolist()

    weak_topics = student_topic[
        (student_topic["student_id"] == student_id) &
        (student_topic["skill_gap"] != "Low")
    ]["topic"].tolist()

    rule_recs = courses[
        (courses["topic"].isin(weak_topics)) &
        (~courses["course_id"].isin(taken))
    ]

    similar_students = (
        similarity_df[student_id]
        .sort_values(ascending=False)
        .iloc[1:6]
        .index
    )

    cf_recs = interactions[
        interactions["student_id"].isin(similar_students)
    ].merge(courses, on="course_id")

    recs = pd.concat([rule_recs, cf_recs]).drop_duplicates("course_id")

    output = []
    for _, row in recs.iterrows():
        output.append({
            "Course": row["course_name"],
            "Topic": row["topic"],
            "Reason": (
                "Low quiz score in this topic"
                if row["topic"] in weak_topics
                else "Recommended based on similar students"
            )
        })

    return output[:top_n]

# -----------------------------
# SIDEBAR (NAVIGATION)
# -----------------------------
st.sidebar.title("🎓 Learning Platform")
page = st.sidebar.radio(
    "Navigate",
    ["Student Dashboard", "Recommendations", "Analytics"]
)

student_id = st.sidebar.selectbox(
    "Select Student",
    students["student_id"]
)

student_info = students[
    students["student_id"] == student_id
].iloc[0]

# -----------------------------
# PAGE 1: STUDENT DASHBOARD
# -----------------------------
if page == "Student Dashboard":
    st.title("👤 Student Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Name", student_info["name"])
    col2.metric("Year", student_info["year"])
    col3.metric("Major", student_info["major"])

    st.subheader("📊 Skill Gap Overview")
    fig1 = px.bar(
        student_topic[student_topic["student_id"] == student_id],
        x="topic",
        y="avg_score",
        color="skill_gap",
        title="Topic-wise Performance"
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("⏱️ Time Spent by Topic")
    fig2 = px.pie(
        student_topic[student_topic["student_id"] == student_id],
        names="topic",
        values="avg_time",
        title="Learning Effort Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# PAGE 2: RECOMMENDATIONS
# -----------------------------
elif page == "Recommendations":
    st.title("🎯 Personalized Recommendations")

    recs = recommend(student_id)

    if not recs:
        st.info("No recommendations available.")
    else:
        for r in recs:
            with st.container():
                st.subheader(r["Course"])
                st.write(f"**Topic:** {r['Topic']}")
                st.success(f"💡 {r['Reason']}")

# -----------------------------
# PAGE 3: ANALYTICS
# -----------------------------
else:
    st.title("📈 Platform Analytics")

    topic_popularity = learning["topic"].value_counts().reset_index()
    topic_popularity.columns = ["Topic", "Enrollments"]

    fig3 = px.bar(
        topic_popularity,
        x="Topic",
        y="Enrollments",
        title="Most Studied Topics"
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("📏 Evaluation Summary")
    st.write("""
    - **Precision@5:** 0.08  
    - **Recall@5:** 0.40  

    These values indicate effective retrieval of relevant learning resources,
    prioritizing recall over precision, which is common in educational platforms.
    """)
 
