from fastapi import FastAPI
from pydantic import BaseModel
from backend.core.pipeline import answer_query

app=FastAPI()

class Query(BaseModel):
    persona:str
    question:str
    document:str

@app.post("/query")
def query(q:Query):
    return answer_query(q.persona,q.question,q.document)
