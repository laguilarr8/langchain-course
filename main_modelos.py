import os
import certifi
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Solucionar el problema de red (ya comprobado)
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

# 2. Cargar tu nueva clave
load_dotenv(override=True)
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: No se detectó ninguna clave en el .env")
    exit()

genai.configure(api_key=api_key)

print("\n=== 1. MODELOS PERMITIDOS PARA TU CLAVE ===")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ {m.name}")
except Exception as e:
    print(f"❌ Error al consultar la lista: {e}")

print("\n=== 2. PRUEBA DE MENSAJE DIRECTO (Sin LangChain) ===")
try:
    # Intentamos con el nombre por defecto
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Hola, responde únicamente con la palabra: EXITO.")
    print(f"🤖 Gemini dice: {response.text}")
except Exception as e:
    print(f"❌ Error al enviar mensaje: {e}")