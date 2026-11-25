from fastapi import FastAPI, HTTPException # 다른 도구 가져오기
from pydantic import BaseModel # 데이터 모양을 정하고 검사해주는 설계도

# 앱
app = FastAPI() # 어떤 주소로 오면 어떤 함수로 실행할지

# 데이터 모양 약속
class PostIn(BaseModel):
    title: str
    content: str

# 저장소
# 함수 바깥에 있으니 서버가 켜질 때 딱 한 번 만들어짐
# 이후의 모든 요청이 이 리스트 하나를 같이 씀
# 컴퓨터 메모리에만 있어서 서버가 꺼지면 사라짐
posts = [] # DB 대신 쓰는 리스트
next_id = 1 # 다음 글에 붙일 번호

# 도우미 함수

# 경로 함수
@app.get("/") # / 주소로 get 요청 시 아래 함수 실행
def home(): # home 함수 정의
    # 딕서녀리를 fastapi가 브라우저가 알아듣는 json 형식으로 바꿔서 돌려줌
    return {"message": "안녕하세요"} 

# /posts 주소로 post 요청 시 아래 함수 실행
# 201은 새로 만들어졌다는 뜻
@app.post("/posts", status_code=201)
def create_post(body: PostIn): # 요청 본문을 postin 모양으로 읽어서 body에 넣어줌
    global next_id # 함수 안에서 함수 밖의 next_id의 값을 바꾸기 위해
    # 저장할 글을 딕셔너리로 만들기
    post = {"id": next_id, "title": body.title, "content": body.content}
    posts.append(post)
    next_id += 1
    return post

@app.get("/posts")
def list_posts():
    return posts

