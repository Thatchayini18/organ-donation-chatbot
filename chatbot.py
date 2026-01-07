def chatbot_response(user_input):
    text = user_input.lower()

    if "donor" in text:
        return (
            "Thank you for your interest in organ donation ❤️\n\n"
            "I will guide you through eligibility verification and registration."
        )

    elif "recipient" in text or "need organ" in text:
        return (
            "I understand your situation.\n\n"
            "I will assess medical urgency and prioritize your case."
        )

    elif "status" in text:
        return (
            "Your request is under evaluation.\n"
            "You will be notified immediately when a match is found."
        )

    else:
        return (
            "I can help you with:\n"
            "- Donor registration\n"
            "- Recipient priority\n"
            "- Match status\n"
            "- Organ donation information"
        )
