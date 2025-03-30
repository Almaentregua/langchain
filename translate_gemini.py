import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
os.environ.get("GOOGLE_API_KEY")

# Inicializamos el modelo Gemini
chat = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
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