from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 設定 CORS 規則，允許前端的正式環境域名
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://stockforest.charlestw.dev",  # 允許正式環境的前端
        "http://localhost:5173",  # 允許本地開發
    ],
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有請求方法 (GET, POST, PUT, DELETE...)
    allow_headers=["*"],  # 允許所有標頭
)

@app.get("/predict/{stock_id}")
async def predict(stock_id: str):
    return {"data": stock_id}
