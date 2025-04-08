from scapy.all import rdpcap, ICMP
from colorama import Fore, Style, init

init(autoreset=True)

palabras_comunes = {
    "el", "la", "de", "que", "y", "en", "a", "los", "se", "no", "un", "por",
    "con", "una", "su", "para", "es", "al", "lo", "como", "más", "pero", "sus", "le"
}

def limpiar_relleno(mensaje):
    inicio = 0
    while inicio < len(mensaje) and mensaje[inicio] == mensaje[0]:
        inicio += 1
    fin = len(mensaje) - 1
    while fin >= 0 and mensaje[fin] == mensaje[-1]:
        fin -= 1
    return mensaje[inicio:fin+1]

def analizar_pcapng(archivo):
    paquetes = rdpcap(archivo)
    mensaje_cifrado = ""
    for paquete in paquetes:
        if ICMP in paquete and paquete[ICMP].type == 8:
            try:
                char = bytes(paquete[ICMP].payload).decode('utf-8', errors='ignore')[0]
                mensaje_cifrado += char
            except:
                continue
    return mensaje_cifrado

def descifrar_cesar(texto, corrimiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base - corrimiento) % 26 + base)
        else:
            resultado += char
    return resultado

def contar_palabras_comunes(texto):
    palabras = texto.lower().split()
    return sum(1 for palabra in palabras if palabra in palabras_comunes)

def descifrar_archivo(archivo_pcapng):
    mensaje_cifrado = analizar_pcapng(archivo_pcapng)
    mensaje_cifrado = limpiar_relleno(mensaje_cifrado)

    print(f"\nMensaje cifrado limpio: {mensaje_cifrado}\n")

    resultados = []
    mejor_score = -1

    for corrimiento in range(1, 26):
        mensaje_descifrado = descifrar_cesar(mensaje_cifrado, corrimiento)
        score = contar_palabras_comunes(mensaje_descifrado)
        resultados.append((corrimiento, mensaje_descifrado, score))
        if score > mejor_score:
            mejor_score = score

    for corrimiento, texto, score in resultados:
        if score == mejor_score:
            print(Fore.GREEN + f"[{corrimiento:02}] {texto}")
        else:
            print(f"[{corrimiento:02}] {texto}")

if __name__ == "__main__":
    archivo_pcapng = input("Introduce la ruta del archivo .pcapng: ").strip().strip('"')
    descifrar_archivo(archivo_pcapng)
