import requests
import json

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3:latest",
        "prompt": "以中文回答我，台灣最適合AI發展的領域是什麼？",
        "stream": True  # 保持流式開啟
    },
    stream=True
)

full_response = ""
for line in response.iter_lines():
    if line:
        chunk = json.loads(line)
        full_response += chunk.get("response", "")
        print(chunk.get("response", ""), end="", flush=True)  # 即時顯示

print("\n\n=== 完整回答 ===")
print(full_response)