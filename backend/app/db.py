# 假裝連線到資料庫（先用變數模擬資料庫內容）
fake_db = {
    "stocks": [
        {"symbol": "AAPL", "price": 172.5},
        {"symbol": "TSLA", "price": 720.1}
    ]
}

def get_stocks():
    """
    功能：取得假資料庫中的股票資訊
    """
    return fake_db["stocks"]

