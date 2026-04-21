import os
import certifi
from dotenv import load_dotenv

# 1. Configurar los certificados
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

# 2. 🔥 CAMBIO CLAVE: Forzar la lectura del archivo .env actual
load_dotenv(override=True)

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from langsmith import wrappers

def main():
    # Pequeño chequeo de seguridad
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERROR: No se encontró ninguna clave en el archivo .env")
        return
    elif api_key.endswith("Lk1Q"):
        print("⚠️ ALERTA: ¡Tu código sigue leyendo la clave vieja y bloqueada!")
        print("Asegúrate de haber guardado el archivo .env con la clave nueva.")
        return

    information = "Nicolas Maquiavelo ..."

    summary_template = """
    dada la información {information} sobre una persona, quiero que crees:
    1. Un resumen corto
    2. dos datos interesantes sobre ella
    3. edad y patrimonio
    4. mejores frases y libros
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # 3. Usamos el modelo estándar
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # gemini-2.5-flash 
        temperature=0,
        request_timeout=30  
    )

    chain = summary_prompt_template | llm

    try:
        response = chain.invoke({"information": information})
        print("\n=== RESPUESTA DE GEMINI ===")
        print(response.content)
    except Exception as e:
        print(f"\nOcurrió un error al conectar con la API: {e}")

if __name__ == "__main__":
    main()