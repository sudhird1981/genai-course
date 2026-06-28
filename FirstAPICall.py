from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
print("Client Created Successfully...")

messages = [
    {
        "role" : "system",
        "content" : "you are a helpful assistant. Keep answers short and simple."
    },
    {
        "role" : "user",
        "content" : "what is artifical intelligence? Explain in 2 lines."
        
    }
]

print("Messages build. let's go to actual call")
print("API call start")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = messages
    )

print("---------------------")
answer = response.choices[0].message
print("RAW response")
print(response)
print("---------------------")
print("This is AI Answer")
answer = response.choices[0].message.content
print("ai sys")
print(answer)
print("---------------------")

import json
#json.dumps() #converts python dictionary to json
#json.loads() #convers json to python dictionary
student = {"name":"sunidhi","city":"pune","course":"genai"}
print(student)
print(json.dumps(student,indent=2))

print("Structured response--------------")
struct_response = response.model_dump()
struct_response1 = json.dumps(struct_response,indent=2)
print(struct_response1)
