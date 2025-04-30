# Importing libraries
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq
import streamlit as st
import os

# Credential and Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "ChatBot with LLM"
os.environ["GOOGLE_API_KEY"] = "AIzaSyD3jjlk9rl6FBUASv21T1aBAFo_h_R6rTk"
os.environ["HF_TOKEN"] = "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"
os.environ["GROQ_API_KEY"] = "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"

# Arxiv and wikipedia tools
api_wrapper_wiki = WikipediaAPIWrapper(top_k_result = 1, doc_content_chars_max = 300)
wiki = WikipediaQueryRun(api_wrapper = api_wrapper_wiki)

api_wrapper_arxiv = ArxivAPIWrapper(top_k_result = 1, doc_content_chars_max = 300)
arxiv = ArxivQueryRun(api_wrapper = api_wrapper_arxiv)

search = DuckDuckGoSearchRun(name = "Search")                           # Search from the web


# Streamlit interface
st.title("🧠 LangChain Agents: Chat Smarter with Live Search 🔍🤖")
'''
In this example we are using streamlit Callback Handler to display the thoughts and action of an agent in an interactiva 
Streamlit app.  
'''
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your GROQ-API key:", type = "password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role" : "Assistant", "content" : "Hi I'm a chat bot who can search the web. How can I help you!"}
    ]
    
for i in st.session_state.messages:                            # Iterates through each chat message stored in the session state
    st.chat_message(i["role"]).write(i["content"])             # Displays the content of the message inside the chat message bubble
    
if prompt:=st.chat_input(placeholder = "Ask anything..."):
    st.session_state.messages.append({"role" : "user", "content" : prompt})    # user's input is appended to the chat history
    st.chat_message("user").write(prompt)                                      # Displays the user’s input right away in the Streamlit chat bubble
    
    llm = ChatGroq(groq_api_key = api_key, model_name = "gemma2-9b-it", streaming = True)
    tools = [search, arxiv, wiki]
    
    search_agent = initialize_agent(tools, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors = True)
    
    with st.chat_message("assistant"):                                                    # This creates a chat message container specifically for the assistant's reply.
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts = False)     # It allows you to visualize each action/observation the agent performs  
        response = search_agent.run(st.session_state.messages, callbacks = [st_cb])       # Runs the agent using the entire message history (st.session_state.messages) as input.
        st.session_state.messages.append({"role" : "assistant", "content" : response})    # Saves the assistant's new response in the session's chat history
        st.write(response) 