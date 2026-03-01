# AI Research Agent

A tool-augmented structured research assistant built using LangChain 1.x and GPT-5.2.

## Features
- Web search (DuckDuckGo)
- Wikipedia integration
- Structured Pydantic outputs
- Automatic file saving
- Modern LangGraph agent architecture

## Architecture

User Query
   ↓
LangChain Agent (LangGraph)
   ↓
LLM Reasoning (GPT-5.2)
   ↓
External Tools
   • DuckDuckGo Search
   • Wikipedia API
   • File Save Tool
   ↓
Structured Pydantic Output
   ↓
Saved Research File

## Setup

1. Clone repo
2. Create virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Add your API key to a `.env` file:

OPENAI_API_KEY=your_key_here

5. Run:

python main.py