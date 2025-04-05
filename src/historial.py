import getpass
import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from constants.models.gemini import GEMINI_PRO_1_5

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

llm = ChatGoogleGenerativeAI(model=GEMINI_PRO_1_5, temperature=0.4)

chat_history = [SystemMessage(content="Eres un experto en ia y especialmente en llm")]

question = input("Human: ")
while question != "exit":
    chat_history.append(HumanMessage(content=question))
    llm_response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=llm_response.content))
    print(f"IA:{llm_response.content}")
    question = input("Human: ")
