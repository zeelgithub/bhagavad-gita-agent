# 🕉️ Bhagavad Gita AI Agent

An interactive question-answering chatbot built using **LangGraph** agent with custom tool and **VectorStore** to answer questions based on the **Bhagavad Gita**. Users can interact with the app via a simple **Streamlit UI**, asking questions and receiving insightful responses grounded in the Gita's teachings.

---

## ✨ Features

- 💬 Ask any question about the Bhagavad Gita  
- 🔍 Uses semantic search to find relevant verses and explanations  
- 🧠 Built using LangGraph Agent for modular agent control  
- 📚 VectorStore tool for information retrieval  
- ⚙️ Local LLM using **Ollama Chat Model**  
- 🖥️ Simple and responsive Streamlit interface  

---

## 🛠️ Tech Stack

| Component         | Description                                                  |
|------------------|--------------------------------------------------------------|
| **LangGraph**     | To define and manage the agent workflow                     |
| **Agent**         | Tool-executing reactive agent for intelligent responses     |
| **VectorStore**   | Stores embedded Bhagavad Gita content for semantic retrieval|
| **Ollama**        | Local LLM backend for answering questions                   |
| **Streamlit**     | Interactive web UI for real-time user interaction           |
| **Poetry**        | Python dependency and environment manager                   |

---

## 🔄 Model Flexibility

This application currently uses the **Ollama Chat Model** for answering questions, but the architecture is **model-agnostic**. You can swap in other LLMs like:

- **OpenAI GPT-4 / GPT-3.5**
- **Anthropic Claude**
- **Mistral**
- **Google Gemini**

Model differences (e.g., context length, token limits, inference cost) will affect the performance and pricing — choose the one that fits your use case.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/bhagavad-gita-agent.git
cd bhagavad-gita-agent
```
#### 2. Install Dependencies with Poetry

Make sure you have Poetry installed.

Then install the project dependencies and activate the virtual environment:

```bash
poetry install
poetry shell
```

### 3. Run the App
```bash
poetry run streamlit run main.py
```