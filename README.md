# Persona Support Agent

## Overview

Persona Support Agent is an AI-powered customer support chatbot built using Python, Streamlit, and Google Gemini API.

The application detects the user's persona, retrieves relevant information from a knowledge base, and generates context-aware responses.

## Features

- Persona Classification
- Knowledge Base Retrieval (RAG)
- Google Gemini Response Generation
- Streamlit Web Interface

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- dotenv

## Installation

git clone https://github.com/dkeskar717-bot/persona-support-agent.git

cd persona-support-agent

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

## Environment Variables

Create a .env file

GEMINI_API_KEY=YOUR_API_KEY

## Run Application

streamlit run app.py

## Author

Vivek Keskar
