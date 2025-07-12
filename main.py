from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("data/dictionary.json", encoding='utf-8') as f:
    data = json.load(f)

@app.get("/")
def root():
    return {"message": "VeloxG API is running"}

@app.get("/api/3f9a8b7c-search")
def search(q: str = Query(..., min_length=1)):
    results = [item for item in data if q.lower() in item["word"].lower()]
    return {"query": q, "results": results
