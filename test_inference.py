import requests
  
  resp = requests.post("http://localhost:8000/inference", json={"prompt": "Hello"})
  print(f"Status: {resp.status_code}")
  print(f"Response: {resp.json()}")

