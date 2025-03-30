import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Falta la API Key. Seteala como variable de entorno.")

# Inicializamos el modelo Gemini
chat = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    google_api_key=api_key,
    temperature=0.7,
)

pregunta = input("¿Qué querés que el llm traduzca? ")

messages = [
    (
        "system",
        "You are a helpful assistant that translates Spanish to English. Translate the user sentence.",
    ),
    ("human", pregunta),
]

# Enviar mensaje y obtener respuesta
respuesta = chat.invoke(messages)

print("\n🔮 Llm responde:")
print(respuesta)

"""
model.invoke("Hello")

model.invoke([{"role": "user", "content": "Hello"}])

model.invoke([HumanMessage("Hello")])
"""