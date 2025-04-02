import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
os.environ.get("GOOGLE_API_KEY")

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

# Inicializamos el modelo Gemini

# model="models/gemini-1.5-flash",

# Crear una plantilla de prompt para traducciones
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# Encadenar la plantilla con el modelo de Google AI
chain = prompt | llm

pregunta = input("¿Qué querés que el llm traduzca? ")

# Invocar la cadena con parámetros específicos

respuesta = chain.invoke(
    {
        "input_language": "Spanish",
        "output_language": "English",
        "input": pregunta,
    }
)

print("\n🔮 Llm responde:")
print(respuesta)