import streamlit as st
from orchestrator import handle_query
from tinydb import TinyDB

st.title("🧠 Persistent Memory Agent")

db = TinyDB("memory/memory_store.json")
topics = [item["name"] for item in db.all()]
topic_options = topics + ["Start new topic"]

# Initialize session state variables
if "conversation_complete" not in st.session_state:
    st.session_state.conversation_complete = False
if "topic_choice" not in st.session_state:
    st.session_state.topic_choice = None
if "new_topic_name" not in st.session_state:
    st.session_state.new_topic_name = ""

# Select topic or start new
st.session_state.topic_choice = st.selectbox(
    "Choose or create a topic",
    options=topic_options,
    index=0 if st.session_state.topic_choice is None else topic_options.index(st.session_state.topic_choice)
)

# If 'Start new topic' is chosen, show text input
if st.session_state.topic_choice == "Start new topic":
    st.session_state.new_topic_name = st.text_input("Enter new topic name", value=st.session_state.new_topic_name)
    selected_topic = st.session_state.new_topic_name.strip()
else:
    selected_topic = st.session_state.topic_choice

# Input field for user query
user_input = st.text_area("Ask a question or input research note:")

# Submit button
if st.button("Submit") and selected_topic and user_input.strip():
    with st.spinner("Thinking..."):
        response, history = handle_query(selected_topic, user_input)
        st.session_state.conversation_complete = True

    # Show response
    st.subheader("💬 AI Response")
    st.write(response)

    # Show memory log
    st.subheader(f"📜 Topic: {selected_topic}")
    for entry in reversed(history):
        st.markdown(f"**You**: {entry['user']}")
        st.markdown(f"**AI**: {entry['ai']}")

# Action buttons after response
if st.session_state.conversation_complete:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔁 Reask on Same Topic"):
            st.rerun()
    with col2:
        if st.button("🆕 Start New Topic"):
            # Reset session state to start fresh
            st.session_state.conversation_complete = False
            st.session_state.topic_choice = None
            st.session_state.new_topic_name = ""
            st.rerun()
