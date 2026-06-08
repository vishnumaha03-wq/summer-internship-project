import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


def draft_queries(all_findings):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        google_api_key=os.getenv(
            "GOOGLE_API_KEY"
        )
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

    response = chain.invoke(
        {
            "findings": all_findings
        }
    )

    return response.content