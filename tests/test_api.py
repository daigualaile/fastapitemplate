import requests

# 你的 token
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTA1NTI5MjIsInN1YiI6Insnc3ViJzogJ2RhbWlhbyd9In0.tX55U7UZePtivqSEs0TQdI965zW9ed09mOdB5twkQOA"

# 请求头中的认证信息
headers = {
    "Authorization": f"Bearer {token}"
}

# 发送带有认证信息的 GET 请求
response = requests.get("http://localhost:8000/server/getLinks", headers=headers)

# 打印响应
print(response.json())
