from fastapi import FastAPI

app = FastAPI(title="🔥 EMERGENCY TEST 🔥", version="3.0")

@app.get("/")
def emergency():
    return "🚨 EMERGENCY SERVER WORKING 🚨"

@app.post("/convert")
def convert():
    return "🎉 POST /convert WORKING! 🎉