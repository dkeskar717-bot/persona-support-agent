def classify_persona(message):
    message = message.lower()

    if any(word in message for word in ["api", "code", "database", "error"]):
        return "Technical Expert"

    elif any(word in message for word in ["frustrated", "angry", "issue", "urgent"]):
        return "Frustrated User"

    return "Business Executive"