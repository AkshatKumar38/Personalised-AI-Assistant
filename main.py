import streamlit as st
from agents.assistant import get_agent
from db.db import init_db

init_db() # Initialize the database

# Set up the page configuration
st.set_page_config(page_title="Personal Assistant", page_icon=":robot_face:", layout="centered", initial_sidebar_state="auto")
st.title("Personal Assistant")
st.markdown("Ask me anything!, I can help you with your tasks, reminders, and more.\n How can I assist you today?")

if "messages" not in st.session_state: # initialize chat history
    st.session_state.messages = []
    
user_input = st.chat_input(placeholder="Type your message here...") # user input

for message in st.session_state.messages: # display chat history
     with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input}) # add user input to chat history
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            agent = get_agent()
            try:
                response = agent.run(user_input) # get response from agent
            except Exception as e:
                response = f"Error: {str(e)}"
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response}) # add response to chat history
                