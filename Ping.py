from scapy.all import IP, ICMP, send
import time

# Solicita el mensaje al usuario
mensaje = input("Ingresa el mensaje cifrado: ")

# IP de destino (Google DNS)
destino = "8.8.8.8"

# Enviar un paquete por cada carácter
for caracter in mensaje:
    paquete = IP(dst=destino)/ICMP(type=8)/caracter.encode()
    send(paquete, verbose=0)
    print("Paquete enviado.")
    time.sleep(0.5)  # Pausa opcional para simular tráfico humano/normal
