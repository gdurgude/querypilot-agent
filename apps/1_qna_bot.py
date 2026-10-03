from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model = "gemini-3.8-flash")

st.title("YapBuddy - Your AI Chatbot")
st.markdown("My YapBuddy with LangChain and Google Gemini API is ready to chat with you! Type your message below and hit Enter.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


    
query = st.chat_input("Type your message here...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query) 
    res = llm.invoke(query)
    st.chat_message("assistant").markdown(res.content[0]["text"])
    st.session_state.messages.append({"role": "assistant", "content": res.content[0]["text"]})

