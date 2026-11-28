import streamlit as st
from datetime import date
import tasks

SUBJECTS = ["Machine Learning", "Database Systems", "Calculus", "Other"]

st.set_page_config(page_title="StudyBuddy", page_icon="📚")
st.title("StudyBuddy - Student Task Manager")

st.subheader("Add a new task")

with st.form("add_task_form", clear_on_submit=True):
    title = st.text_input("Task title")
    subject = st.selectbox("Subject", SUBJECTS)
    deadline = st.date_input("Deadline", value=date.today())
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    submitted = st.form_submit_button("Add task")

if submitted:
    if title.strip() == "":
        st.error("Please enter a task title.")
    else:
        tasks.add_task(title.strip(), subject, deadline, priority)
        st.success("Task added.")
