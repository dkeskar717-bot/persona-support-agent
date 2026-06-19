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

    # Adaptive Prompting
    if persona == "Technical Expert":
        persona_prompt = """
        You are a Senior Technical Support Engineer.
        Provide detailed technical explanations,
        root cause analysis and troubleshooting steps.
        """

    elif persona == "Frustrated User":
        persona_prompt = """
        You are an empathetic support specialist.
        Acknowledge the user's frustration and provide
        simple step-by-step guidance.
        """

    else:
        persona_prompt = """
        You are a Business Support Executive.
        Provide concise and professional responses.
        Focus on timelines and business impact.
        """

    # Gemini Response
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""
            {persona_prompt}

            Persona:
            {persona}

            Context:
            {context}

            User Query:
            {user_input}

            Answer ONLY using the provided context.
            Adapt your tone based on the persona.
            """
        )

        final_response = response.text

    except Exception:
        final_response = f"""
Based on the knowledge base:

{context}

Note:
AI response is temporarily unavailable, so the answer is being provided directly from the knowledge base.
"""

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
    st.write(final_response)