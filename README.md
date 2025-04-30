
# 🧠 LangChain Agents: Chat Smarter with Live Search 🔍🤖

This repository showcases an interactive chatbot powered by [LangChain](https://www.langchain.com/), integrated with **Streamlit** for a user-friendly UI. The agent is capable of live information retrieval using tools like **Wikipedia**, **Arxiv**, and **DuckDuckGo**, and is powered by the **Groq LLM (gemma2-9b-it)** model for smart and contextual conversation.

## 🔧 Features

- 🔍 Live search using DuckDuckGo
- 📚 Academic research from Arxiv
- 🧾 Summarized content from Wikipedia
- 🤖 Conversational AI powered by Groq (gemma2-9b-it)
- 🧠 Zero-Shot ReAct Agent to intelligently use tools
- 🎯 Integrated tracking with LangSmith
- 🖥️ Real-time visualization using Streamlit

## 🧪 Tech Stack

- `LangChain`: for agent logic and tool integration
- `LangChain Community`: for pre-built tools and wrappers
- `Streamlit`: for creating the web-based chatbot interface
- `Groq LLM`: for powerful, fast inference
- `WikipediaAPIWrapper`, `ArxivAPIWrapper`, `DuckDuckGoSearchRun`: tools for information retrieval

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/langchain-chatbot.git
cd langchain-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit langchain langchain_community langchain_groq duckduckgo-search
```

### 3. Set Environment Variables

Set the following environment variables (or store them in a `.env` file and load them using `python-dotenv`):

```bash
export LANGCHAIN_API_KEY=your_langchain_api_key
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_PROJECT="ChatBot with LLM"
export GOOGLE_API_KEY=your_google_api_key
export HF_TOKEN=your_huggingface_token
export GROQ_API_KEY=your_groq_api_key
```

### 4. Run the App

```bash
streamlit run app.py
```

> You will be prompted to enter your GROQ API key in the sidebar to initialize the LLM.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq](https://groq.com/)
- [DuckDuckGo](https://duckduckgo.com/)
- [ArXiv](https://arxiv.org/)
- [Wikipedia](https://www.wikipedia.org/)

---

🔗 **Made with ❤️ by Chetan**
