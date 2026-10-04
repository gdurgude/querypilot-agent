from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_keenable import KeenableSearch
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver


# Page setup
st.set_page_config(page_title="QueryPilot", page_icon="🐱")

st.title("🐱 QueryPilot")
st.caption("AI assistant with web search")


# Create memory once
if "checkpointer" not in st.session_state:
    st.session_state.checkpointer = MemorySaver()


# Create agent once
if "agent" not in st.session_state:
    llm = ChatGroq(model="openai/gpt-oss-20b")
    search = KeenableSearch()

    st.session_state.agent = create_agent(
        model=llm,
        tools=[search],
        system_prompt="You are a helpful assistant that can answer questions based on the provided context. Use the search tool to find relevant information when needed.",
        checkpointer=st.session_state.checkpointer
    )


# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
question = st.chat_input("Ask a question...")


if question:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)


    # Ask the agent
    response = st.session_state.agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        },
        {
            "configurable": {
                "thread_id": "Gaurav-Agent"
            }
        }
    )


    # Extract answer
    answer = response["messages"][-1].content

    if isinstance(answer, list):
        answer = answer[0]["text"]


    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


    # Show newest AI response with cat
    with st.chat_message("assistant"):
        cat_col, answer_col = st.columns([1, 4])

        with cat_col:
            st.video(
                "assets/cat_talking.mp4",
                autoplay=True,
                muted=True,
                loop=True
            )

        with answer_col:
            st.write(answer)