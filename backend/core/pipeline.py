from backend.core.vector_store import search
from backend.agents.router import route
from backend.core.generator import generate

def answer_query(persona,question,document):
    ctx=search(document,question)
    ctx=route(persona,ctx)
    return {
      "answer": generate(question,ctx),
      "citations": ctx
    }
