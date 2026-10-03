# YapBuddy Chatbot

YapBuddy is a simple AI-powered command-line chatbot built with Python, LangChain, and Google Gemini.

The goal of this project was to understand how LLM-powered applications work in practice, including API integration, environment variables, model responses, error handling, and working with external AI services.

## Features

- Interactive command-line chatbot
- Powered by Google Gemini
- LangChain integration
- Secure API key handling using `.env`
- Continuous question-and-answer interaction
- Clean extraction of AI responses
- Simple architecture that can be extended into a larger GenAI application

## Tech Stack

- Python
- LangChain
- Google Gemini API
- `langchain-google-genai`
- `python-dotenv`

## Project Structure

```text
GenAI-Series/
│
├── apps/
│   └── 1_qna_bot.py
│
├── notebooks/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> The `.env` file is excluded from GitHub because it contains the API key.

## How It Works

```text
User enters a question
        ↓
Python application
        ↓
LangChain
        ↓
Google Gemini API
        ↓
AI-generated response
        ↓
Response displayed in terminal
```

The chatbot sends the user's input to Gemini through LangChain and displays only the generated text response.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/gdurgude/yapbuddy-chatbot.git
cd yapbuddy-chatbot
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit this file to GitHub.

### 5. Run YapBuddy

```powershell
python apps/1_qna_bot.py
```

## Example

```text
User: Hi

AI: Hello! How can I help you today?

User: What is AI engineering?

AI: AI engineering focuses on designing, building, evaluating,
and deploying software systems powered by artificial intelligence.
```

## What I Learned

While building YapBuddy, I learned how to:

- Connect a Python application to an LLM
- Use LangChain to interact with Gemini
- Work with API keys and environment variables
- Create and use Python virtual environments
- Install and manage Python dependencies
- Understand structured model responses
- Extract only the generated text from model output
- Troubleshoot missing Python packages
- Debug API model availability issues
- Handle Gemini `429` quota errors
- Understand temporary `503` model availability errors
- Work with Git and GitHub repositories

## Errors I Encountered

A few real issues came up while building the project.

### Model Not Found

An older Gemini model returned a `404 NOT_FOUND` error because it was no longer available for new users.

This taught me that AI model availability and API versions can change over time.

### Service Unavailable

Gemini occasionally returned:

```text
503 UNAVAILABLE
```

This happens when the model is temporarily under heavy demand.

In a production application, this should be handled using retry logic and fallback behavior.

### Rate Limit

The API also returned:

```text
429 RESOURCE_EXHAUSTED
```

after reaching the free-tier request quota.

This highlighted the importance of monitoring API limits, costs, and usage when building AI applications.

## Future Improvements

YapBuddy is currently a lightweight chatbot, but I plan to extend it with:

- Conversation memory
- Streaming responses
- Retry and rate-limit handling
- Prompt templates
- FastAPI backend
- Streamlit interface
- Chat history
- RAG with document retrieval
- Vector embeddings
- Vector database integration
- Source citations
- LLM evaluation
- Multiple model support

## Why I Built This

I built YapBuddy as part of my practical learning in AI engineering.

Instead of only studying LLM concepts theoretically, I wanted to build working AI applications and understand how each component behaves in real systems.

This project is the starting point for a larger GenAI learning series covering RAG, embeddings, vector databases, evaluation, agents, and production AI systems.

## Author

**Gaurav Durgude**

GitHub: [gdurgude](https://github.com/gdurgude)