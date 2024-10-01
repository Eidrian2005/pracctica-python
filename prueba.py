
# Primera prueba

# def Saludo():
#     nombre = input("Ingrese su nombre:")
#     print("Bienvenido,",nombre)
#     return

# def nota():
#     Lista = [80, 70, 90]
#     valores = len(Lista)
#     suma = 0

#     for numero in Lista:
#         suma += numero

#     promedio = suma / valores
#     print(f"El promedio es:{promedio}")
#     return

# Saludo()
# nota()

# Segunda Prueba

# def RangoEdades():
#     Nombre, Edad = [input("Ingrese su nombre:"), int(input("Ingrese su edad:"))]
    
    
#     if Edad < 13:
#         print(Nombre, "Es un niño")
#     elif Edad >= 13 and Edad < 18:
#         print(Nombre,"Es un adolencente")
#     elif Edad >= 18 and Edad < 60:
#         print(Nombre, "Es un adulto")
#     elif Edad >= 60:
#         print(Nombre, "Es un adulto mayor")
#     return

# RangoEdades()


# Tercera prueba


# def ListaNumeros():
#     numeros = input("Agregue numeros: ")
#     lista = [int(num.strip()) for num in numeros.split(",")]
#     par = 0
#     impares = 0
#     for numero in lista:
#         if numero % 2 == 0:
#             par += 1
#         else:
#             impares += 1
    
#     print(f"Numeros pares: {par}")
#     print(f"Numeros impares: {impares}")

# ListaNumeros()

# Cuarta Prueba


def ContarVocales():
    frase = input("Agregue una frase: ")
    print(frase)
    contador = 0
    print(contador)
    
    for c in frase:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            contador += 1
    return contador



ContarVocales()