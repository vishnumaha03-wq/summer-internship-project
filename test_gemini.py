import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6I6sWEuhZ1QML_LXTcY30tsHW1uy0DMvbe1hf2QYJgRWg"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

response = llm.invoke(
    "Say hello."
)

print(response.content)