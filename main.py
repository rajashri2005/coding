import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process
from agents import researcher, analyst, writer, editor, manager
from tasks import create_tasks

st.title("🚀 AI Agent Pipeline")

# Sidebar for Accountability
with st.sidebar:
    st.header("Agent Accountability")
    st.write("1. 🔍 Researcher")
    st.write("2. 📊 Analyst")
    st.write("3. ✍️ Writer")
    st.write("4. 🛠 Editor")
    st.write("5. 👑 Manager")

# Chat Input
user_topic = st.chat_input("Enter a topic for the agents to process...")

if user_topic:
    st.chat_message("user").write(user_topic)
    
    with st.chat_message("assistant"):
        with st.status("Agents are working...", expanded=True) as status:
            # Create Pipeline
            task_list = create_tasks(user_topic, researcher, analyst, writer, editor, manager)
            
            crew = Crew(
                agents=[researcher, analyst, writer, editor, manager],
                tasks=task_list,
                process=Process.sequential,
                verbose=True
            )
            
            # Execute
            result = crew.kickoff()
            status.update(label="Process Complete!", state="complete", expanded=False)
        
        st.markdown("### Final Report")
        st.markdown(result)