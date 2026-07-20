def classify_email(email: str) -> str:
    text = email.lower()

    if "refund" in text:
        return "Refund"

    if "invoice" in text:
        return "Invoice"

    if "quotation" in text or "quote" in text:
        return "Sales"

    if "meeting" in text:
        return "Meeting"

    if "job" in text or "resume" in text:
        return "Recruitment"

    return "General"