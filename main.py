from fastapi import FastAPI # 다른 도구 가져오기

app = FastAPI()

@app.get("/")
def home():
    return {"message": "안녕하세요"}

