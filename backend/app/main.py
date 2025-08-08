# 匯入 FastAPI 框架
from fastapi import FastAPI
# 匯入跨來源資源共用設定（讓前端網頁可連後端 API）
from fastapi.middleware.cors import CORSMiddleware

# 建立 FastAPI 應用
app = FastAPI()

# 設定允許的前端來源（這裡 * 表示任何來源都允許，方便測試）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許的網域
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有 HTTP 方法（GET、POST…）
    allow_headers=["*"],  # 允許所有標頭
)

# 建立一個最簡單的 GET API
@app.get("/hello")  # 當有人訪問 /hello 時會執行這個函式
def read_hello():
    """
    功能：回傳一段文字給前端
    """
    return {"message": "Hello from FastAPI!"}  # 回傳 JSON 格式
