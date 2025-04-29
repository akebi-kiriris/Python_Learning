import ollama

# 設定你的問題
prompt = "用繁體中文列出五個 Python 的優點"

# 呼叫模型
response = ollama.generate(
    model="llama3:latest",
    prompt=prompt
)

# 打印結果
print("模型回覆：")
print(response["response"])