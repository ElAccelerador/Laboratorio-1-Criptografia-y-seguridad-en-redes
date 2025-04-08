# Laboratorio-1-Criptografia-y-seguridad-en-redes 🔐

Este repositorio contiene el desarrollo del Laboratorio 1, enfocado en el cifrado César y el envío de mensajes cifrados a través del protocolo ICMP utilizando Python, Scapy y análisis de tráfico con Wireshark.

## 📂 Archivos principales

- `Cifrado Cesar.py`: Script para cifrar un mensaje usando el algoritmo de cifrado César. El usuario ingresa el mensaje y el desplazamiento.
- `Ping.py`: Envía el mensaje cifrado, carácter por carácter, utilizando paquetes ICMP hacia una IP pública (por defecto, 8.8.8.8).
- `Descifrar Cesar.py`: Lee una captura de red (`.pcapng`), reconstruye el mensaje oculto desde los paquetes ICMP y prueba todos los posibles desplazamientos del cifrado César para determinar el texto original.

## ⚙️ Requisitos

- Python 3.x
- [Scapy](https://scapy.readthedocs.io/en/latest/): `pip install scapy`
- [Colorama](https://pypi.org/project/colorama/): `pip install colorama`
- Wireshark (para generar y analizar capturas `.pcapng`)

## 🚀 Cómo usar

1. **Cifrar un mensaje**  
   Ejecutá `Cifrado Cesar.py`, ingresá tu mensaje y el desplazamiento.

2. **Enviar el mensaje**  
   Ejecutá `Ping.py` y pegá el mensaje cifrado. Se enviará carácter por carácter mediante ICMP.

3. **Capturar con Wireshark**  
   Antes de ejecutar el envío, iniciá la captura en Wireshark. Cuando termine, detené la captura y guardala como `.pcapng`.

4. **Descifrar el mensaje**  
   Ejecutá `Descifrar Cesar.py`, ingresá la ruta del archivo `.pcapng`, y el script mostrará todos los posibles descifrados. El más probable se resalta en verde.

## 🧠 Comentarios

Este laboratorio demuestra cómo mensajes cifrados pueden camuflarse dentro de tráfico de red común (pings) y cómo puede ser posible recuperarlos desde una captura. También se usó IA generativa como apoyo para agilizar el desarrollo, aunque fue necesario ajustar y corregir manualmente partes del código.

## 📸 Ejemplo de salida

```bash
Introduce la ruta del archivo .pcapng: CapturaICMP.pcapng

Mensaje cifrado limpio: larycxpajorj h bnpdarmjm nw anmnb

[09] criptografia y seguridad en redes
