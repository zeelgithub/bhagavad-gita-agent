# app.py

import streamlit as st
from langchain_ollama import ChatOllama
from data_utils import load_and_split_documents, create_vector_store
from gita_agent import bhagavad_gita_agent

st.set_page_config(
    page_title="Bhagavad Gita – Divine Companion", page_icon="🕉️")

st.markdown(
    """
    <div style='text-align: center; font-size: 24px; white-space: nowrap; font-weight: 600;'>
        🕉️ Bhagavad Gita – Divine Companion
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "Ask questions about the Bhagavad Gita and receive precise responses based on scripture.")


@st.cache_resource
def setup_agent():
    split_docs = load_and_split_documents()
    vector_store = create_vector_store(split_docs, model_name="llama2")
    llm = ChatOllama(model="mistral")
    agent_executor = bhagavad_gita_agent(llm, vector_store)
    return agent_executor


agent_executor = setup_agent()


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if prompt := st.chat_input("What did Krishna say to Arjuna in Chapter 2?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = agent_executor.invoke({
                    "messages": [{"role": "user", "content": prompt}]
                })
                output = response['messages'][-1].content
                st.markdown(output)
                st.session_state.messages.append(
                    {"role": "assistant", "content": output})
            except Exception as e:
                error_msg = f"❌ Error: {e}"
                st.error(error_msg)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_msg})
