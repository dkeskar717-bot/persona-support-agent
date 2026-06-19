from src.classifier import classify_persona
from src.rag_pipeline import retrieve_context
import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.title("Persona Support Agent")

user_input = st.text_area("Enter your message")

if st.button("Submit"):

    # Persona Detection
    persona = classify_persona(user_input)

    # RAG Retrieval
    context = retrieve_context(user_input)

    # Escalation Logic
    escalation_words = [
        "refund",
        "billing",
        "duplicate charge",
        "legal",
        "lawsuit"
    ]

    escalate = any(
        word in user_input.lower()
        for word in escalation_words
    )

    # Gemini Response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Persona: {persona}

        Context:
        {context}

        User Query:
        {user_input}

        Answer the user based on the provided context.
        """
    )

    st.write("### Persona")
    st.write(persona)

    st.write("### Retrieved Context")
    st.write(context)

    if escalate:
        st.error("Escalation Required")

        st.write("### Escalation Report")

        st.json({
            "escalate": True,
            "reason": "Billing/Legal Issue",
            "summary": user_input
        })

    st.write("### Response")
    st.write(response.text)