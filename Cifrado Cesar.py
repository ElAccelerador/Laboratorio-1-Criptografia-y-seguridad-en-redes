def cifrado_cesar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            # Mantener mayúsculas y minúsculas por separado
            base = ord('A') if caracter.isupper() else ord('a')
            # Desplazar el carácter dentro del rango alfabético
            nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo_caracter
        else:
            # Conservar espacios, signos y números sin cambio
            resultado += caracter

    return resultado

# Ingreso por parte del usuario
mensaje = input("Ingresa el mensaje a cifrar: ")
while True:
    try:
        desplazamiento = int(input("Ingresa el desplazamiento (número entero): "))
        break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Cifrado
mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)
print(f"\nMensaje cifrado: {mensaje_cifrado}")

