from wiki_search import wiki_search
from speech_engine import speak

def answer_question(q: str) -> bool:
    """
    Try to answer user question. Return True if handled, False if not.
    For now: try wiki search for small queries, otherwise return False.
    """
    q = (q or "").strip()
    if not q:
        return False
    # Simple heuristic
    lower = q.lower()
    if any(x in lower for x in ("who", "what", "when", "where")):
        wiki_search(q)
        return True
    # Otherwise not handled
    return False
