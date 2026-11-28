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

st.subheader("Your tasks")

selected_subject = st.selectbox("Filter by subject", ["All"] + SUBJECTS)

task_list = tasks.get_sorted_tasks(selected_subject)

if len(task_list) == 0:
    st.info("No tasks yet. Add your first task above.")

for task in task_list:
    col1, col2, col3 = st.columns([6, 1, 1])

    if task["done"]:
        col1.write(f"~~{task['title']}~~ ({task['subject']}, due {task['deadline']})")
    else:
        col1.write(f"**{task['priority']}**: {task['title']} ({task['subject']}, due {task['deadline']})")

    if not task["done"]:
        if col2.button("Done", key=f"done_{task['id']}"):
            tasks.mark_done(task["id"])
            st.rerun()

    if col3.button("Delete", key=f"delete_{task['id']}"):
        tasks.delete_task(task["id"])
        st.rerun()
