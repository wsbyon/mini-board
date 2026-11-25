from fastapi import FastAPI # 다른 도구 가져오기

app = FastAPI() # 어떤 주소로 오면 어떤 함수로 실행할지

@app.get("/") # / 주소로 get 요청 시 아래 함수 실행해줘
def home(): # home 함수 정의
    # 딕서녀리를 fastapi가 브라우저가 알아듣는 json 형식으로 바꿔서 돌려줌
    return {"message": "안녕하세요"} 


