1




# Custom version
# mohist / catserver   Install forge   first
# purpur               Install fabric  first
# snapshot             Install vanilla first

# Ngrok region
# Code           Place
#-----------     ---------------------------
# ap	          Asia/Pacific (Singapore)
# au		  Australia (Sydney)
# eu		  Europe (Frankfurt)
# in		  India (Mumbai)
# jp		  Japan (Tokyo)
# sa		  South America (São Paulo)
# us		  United States (Ohio)
# us-cal-1	  United States (California)















import os
import requests
import base64
import schedule
import time
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running"

def press_space():
    print("Simulación de presionar espacio")
    # Aquí puedes agregar cualquier otra funcionalidad que necesites

def say_hello():
    print("Hola")

def restart_server():
    print("Reiniciando el servidor...")
    os.execv(__file__, os.sys.argv)  # Reiniciar el servidor Flask

def download_latest_release(download_path='.'):
    mirror = "https://elyxdev.github.io/latest"
    pet = requests.get(mirror)
    if pet.status_code == 200:
        data = pet.json()
        url = data.get('url')
        version = url.split("/")[-1]
        pathto = os.path.join(download_path, version)
        with open(pathto, 'wb') as archivo:
            archivo.write(requests.get(url).content)
        return version

def main():
    # Programar la ejecución de press_space() cada 3 horas
    schedule.every(3).hours.do(press_space)

    # Programar la ejecución de say_hello() cada 10 minutos
    schedule.every(10).minutes.do(say_hello)

    if not os.path.exists("./.gitignore"):
        big = "L3dvcmtfYXJlYQ0KL3NlcnZpZG9yX21pbmVjcmFmdA0KL21pbmVjcmFmdF9zZXJ2ZXINCi9zZXJ2aWRvcl9taW5lY3JhZnRfb2xkDQovdGFpbHNjYWxlLWNzDQovdGhhbm9zDQovYmtkaXINCi92ZW5kb3INCmNvbXBvc2VyLioNCmNvbmZpZ3VyYXRpb24uanNvbg0KY29uZmlndXJhY2lvbi5qc29uDQoqLnR4dA0KKi5weWMNCioub3V0cHV0"
        dec = base64.standard_b64decode(big).decode()
        with open(".gitignore", 'w') as giti:
            giti.write(dec)
    flnm = download_latest_release()
    if flnm.split(".")[-1] == "pyc":
        os.system(f"python3 {flnm}")
    else:
        os.system(f"chmod +x {flnm} && ./{flnm}")

    # Ejecutar el bucle principal de schedule por 3 horas
    start_time = time.time()
    while time.time() - start_time < 3 * 60 * 60:  # 3 horas en segundos
        schedule.run_pending()
        time.sleep(1)
    
    # Después de 3 horas, reiniciar el servidor Flask
    restart_server()

if __name__ == "__main__":
    # Agregar una pausa para permitir copiar la URL
    print("Esperando 60 segundos para copiar la URL de Codespaces...")
    time.sleep(1)
    
    # Obtener el nombre del Codespace y mostrar la URL de previsualización de GitHub si está disponible
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        codespace_url = f"https://{codespace_name}-8080.githubpreview.dev/"
        print(f"La URL de tu Codespace es: {codespace_url}")
    else:
        print("No se pudo determinar la URL del Codespace.")

    # Iniciar el servidor Flask en un hilo separado
    server_thread = Thread(target=lambda: app.run(host='0.0.0.0', port=8080))
    server_thread.start()

    # Ejecutar la función principal
    main()

