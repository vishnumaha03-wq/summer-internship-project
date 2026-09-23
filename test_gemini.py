import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Pull the API key safely from your local secret .env notepad
load_dotenv()

# 2. Extract the key to check that it exists
api_key = os.getenv("GEMINI_API_KEY")

# 3. Initialize the model using the updated gemini-3.6-flash engine
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# 4. Prompt the AI and get a response
response = llm.invoke("Say hello.")

# 5. Print the output text directly into your terminal screen
print(response.content)