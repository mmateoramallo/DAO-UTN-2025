import psutil
import time
import tkinter as tk
from tkinter import messagebox

nombre_programa = "LeagueClientUxRender.exe"

def programa_en_ejecucion(nombre):
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'].lower() == nombre.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def mostrar_alerta():
    ventana = tk.Tk()
    ventana.withdraw()  
    messagebox.showwarning("¡ALERTA!", "⚠️ Cerrá esto y ponete a estudiar 😤")
    ventana.destroy()

if __name__ == "__main__":
    print("🔍 Monitoreando League of Legends (Ctrl + C para detener)...\n")

    while True:
        if programa_en_ejecucion(nombre_programa):
            print(f"✅ '{nombre_programa}' está en ejecución.")
            mostrar_alerta()
            time.sleep(10)  # espera un poco antes de volver a mostrar la alerta
        else:
            print(f"❌ '{nombre_programa}' no está en ejecución.")
        time.sleep(5)
