// 這個函式會呼叫後端 API /hello
function getMessage() {
    // 後端 API URL（假設後端在 http://127.0.0.1:8000）
    fetch("http://127.0.0.1:8000/hello")
        .then(response => response.json()) // 把 API 回傳轉成 JSON
        .then(data => {
            // 顯示在網頁上
            document.getElementById("result").innerText = data.message;
        })
        .catch(error => console.error("發生錯誤：", error)); // 錯誤處理
}

