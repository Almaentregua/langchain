import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

# model="models/gemini-1.5-flash",
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

parser = StrOutputParser()
chain = prompt | llm | parser

question = input("¿Qué querés que el llm traduzca? ")

response = chain.invoke(
    {
        "input_language": "Spanish",
        "output_language": "English",
        "input": question,
    }
)

print("\n🔮 Llm responde:")
print(response)