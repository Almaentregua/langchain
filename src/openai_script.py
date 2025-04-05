import getpass
import os

from dotenv import load_dotenv
from langchain_core.messages import (AIMessage, HumanMessage, SystemMessage,
                                     trim_messages)
from langchain_openai import ChatOpenAI

from constants.models.openai import GPT_TURBO_3_5

load_dotenv()

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

# models
# gpt-4o
model = ChatOpenAI(model=GPT_TURBO_3_5, temperature=0.2)

messages = [
    SystemMessage(content="Eres un asistente útil."),
    HumanMessage(content="Me ayudas a organizar las tareas del dia?"),
    AIMessage(content="Claro! Que tareas necesitas completar hoy?"),
    HumanMessage(
        content="Tengo que enviar un correo importante, hacer ejercicio y estudiar para un examen"
    ),
    AIMessage(
        content="Aquí tienes tu lista de tareas: 1. Enviar correo. 2. Hacer ejercicio. 3. Estudiar para el examen"
    ),
]

response = model.invoke(messages)
print(response)

trimmed_messages = trim_messages(
    messages,
    max_tokens=5,
    strategy="last",
    token_counter=ChatOpenAI(model="gpt-4o"),
    include_system=True,
)

# print(trimmed_messages)
