from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    return {"filename": file.filename, "message": "파일 업로드 성공!"}