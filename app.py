import streamlit as st
from reviewer import analyze_conversation

st.set_page_config(page_title="Conversation Reviewer", layout="centered")

st.title("🤖 Conversation Review System")
st.write("Evaluate text-driven conversations between user and virtual assistant")

user_input = st.text_area("User Message", height=150)
bot_input = st.text_area("Bot Reply", height=150)

if st.button("Analyze Conversation"):
    if user_input.strip() == "" or bot_input.strip() == "":
        st.warning("Please enter both messages.")
    else:
        results = analyze_conversation(user_input, bot_input)

        st.subheader("📊 Analysis Results")
        for key, value in results.items():
            st.write(f"**{key}:** {value}")
