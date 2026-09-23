import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load the environment variables from your secret .env file
load_dotenv()

def draft_queries(all_findings):
    # Safely pull your API key from the environment
    api_key_val = os.getenv("GEMINI_API_KEY")

    # Initialize the model using the updated 3.6-flash engine and pass the key explicitly
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0,
        max_retries=6,
        google_api_key=api_key_val
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are a senior audit associate.

            Review the findings provided.

            Only discuss issue categories that actually exist.

            Reference specific transaction details wherever possible.

            If a category has no findings, do not mention it.

            Generate a professional client query report suitable for sending to a client.

            Organize findings logically and clearly explain what supporting
            documentation, clarification, or corrective action is required.

            The report should dynamically change based on the findings supplied.

            Use a professional accounting and audit communication style.
            """
        ),
        (
            "human",
            """
            Findings:

            {findings}

            Generate the final client report.
            """
        )
    ])

    chain = prompt | llm
    print("Sending findings to Gemini API now, waiting for response...")
    response = chain.invoke(
        {
            "findings": all_findings
        }
    )

    return response.content
