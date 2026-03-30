# Handles extraction of text from uploaded documents
# Currently supports text files, but structured to extend for PDFs later

def extract_text(file_bytes: bytes) -> str:
    """
    Extract readable text from uploaded file.
    If decoding fails, return empty string instead of crashing.
    """

    if not file_bytes:
        return ""

    try:
        text = file_bytes.decode("utf-8")
    except UnicodeDecodeError:
        text = file_bytes.decode("latin-1", errors="ignore")

    cleaned_text = text.strip()

    return cleaned_text