# Resume analyzer 

import requests
import json
url = "http://localhost:11434/api/chat"
params = {
    "model" : "llama3.2",
    "messages" : [
        {
            "role" : "user",
            "content": "what is a list in python?"
        }
    ],
    "stream" : False

}

response = requests.post(url, json = params)
check = response.status_code
print(check)
if(check == 200):
    data = response.json()
    with open("Report.txt", "w") as file:
        json.dump(data, file, indent=4)
    print(data["message"]["content"])
  