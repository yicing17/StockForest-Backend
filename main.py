from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 設定 CORS 規則，允許前端的正式環境域名
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://stockforest-frontend.zeabur.internal:8080",  # 允許正式環境的前端
        "http://localhost:5173",  # 允許本地開發
    ],
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有請求方法 (GET, POST, PUT, DELETE...)
    allow_headers=["*"],  # 允許所有標頭
)

@app.get("/")
async def root():
    return {"data": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}