import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "AIzaSyDWKDXEKPA2DyNToAdYz9kOBBJSEw2HoYU"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

response = llm.invoke(
    "Say hello."
)

print(response.content)