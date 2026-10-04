# QueryPilot Agent

QueryPilot is a small AI agent I built to learn how tool-using LLM applications work in practice.

The agent runs in a Streamlit chat interface, uses Groq for the language model, and can call a web search tool when it needs current information. I also added conversation memory so it can continue from earlier messages instead of treating every prompt like a brand-new conversation.

One fun detail: when the agent responds, a cat animation appears next to the answer.

## What it does

- Chat with the agent in the browser
- Search the web when current information is needed
- Remember previous messages in the same session
- Continue the conversation naturally
- Display responses in a Streamlit chat interface
- Show a cat animation with AI responses
- Use LangChain and LangGraph for agent behavior and memory

## Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- Groq
- Keenable Search
- `python-dotenv`

## Project Structure

```text
GenAI-Series/
├── apps/
│   └── 2_qna_bot.py
├── assets/
│   └── cat_talking.mp4
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

The `.env` file is not pushed to GitHub because it contains API keys.

## How the agent works

```text
User question
     ↓
Streamlit chat interface
     ↓
LangChain agent
     ↓
Groq LLM
     ↓
Web search tool when needed
     ↓
LangGraph memory
     ↓
Final response
     ↓
Cat animation + answer
```

The agent does not use the search tool for every question. It can answer directly when the model already has enough context, and use search when the question needs current or external information.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/gdurgude/querypilot-agent.git
cd querypilot-agent
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file in the project root and add the API keys required by Groq and the search tool.

Example:

```env
GROQ_API_KEY=your_key_here
```

Add any additional API key required by your search provider as well.

### 5. Run the app

```powershell
streamlit run apps/2_qna_bot.py
```

Streamlit should automatically open the app in your browser.

## What I learned

This project taught me a lot more than just how to call an LLM API.

I learned how an agent can decide when to use a tool, how conversation memory works with a thread ID and checkpointing, and how Streamlit reruns affect application state.

I also ran into real API issues while building it, including rate limits, token limits, temporary service failures, missing packages, and model availability changes. Debugging those problems gave me a much better understanding of what it takes to make an AI application reliable.

## Memory

The agent uses LangGraph's `MemorySaver` so it can remember previous turns during the running session.

For example:

```text
User: My favorite language is Python.

AI: Got it.

User: What language did I say I like?

AI: You said your favorite language is Python.
```

The current memory is in-memory only, so restarting the application clears it.

A future improvement would be to use persistent storage such as SQLite or PostgreSQL.

## Current Limitations

This is still an early version.

A few things I would improve next:

- Persistent memory across app restarts
- Better handling for API rate limits
- Retry logic for temporary failures
- Streaming responses
- Cleaner source citations from search
- Multiple conversations or user sessions
- Better UI styling
- Deployment to a public URL

## Author

**Gaurav Durgude**

GitHub: [gdurgude](https://github.com/gdurgude)
