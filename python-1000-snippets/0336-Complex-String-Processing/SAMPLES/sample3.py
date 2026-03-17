"""Clean and normalize text by removing punctuation & accents."""

import re
import unicodedata


def normalize_text(text: str) -> str:
    # Normalize unicode characters (e.g., accents) and remove diacritics
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    # Remove punctuation and collapse whitespace
    cleaned = re.sub(r"[^\w\s]", "", ascii_text)
    return re.sub(r"\s+", " ", cleaned).strip().lower()


if __name__ == "__main__":
    text = "Héllo   Wörld!  This is a test..."
    print("Cleaned:", normalize_text(text))
