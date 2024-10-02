
# def editor(): 
#     diccionario = {
#     "nombre": "Juan",
#     "edad": 25,
#     "ciudad": "madrid",
#     "trabajo": "programador"
#     }
    
#     llave = input("Cual dato desea cambiar:".lower())
    
#     if llave == "nombre":
#         nuevoNombre = input("Agregue nuevo nombre: ")
#         diccionario ["nombre"] = nuevoNombre
#     elif llave == "edad":
#         nuevaEdad = input("Agregue nueva edad: ")
#         diccionario ["edad"] = nuevaEdad
#     elif llave == "ciudad":
#         nuevaCuidad = input("Agregue nueva ciudad: ")
#         diccionario["ciudad"] = nuevaCuidad
#     elif llave == "trabajo":
#         nuevoTrabajo = input("Agregue nuevo trabajo: ")
#         diccionario["trabajo"] = nuevoTrabajo
    
#     print(diccionario)
#     return

# editor()




#Prueba 2 hacer un menu
# import os

# def menu():
    
#     while True:
#         print("--Precione 1 para juegos")
#         juegos =[
#             "The legend of zelda",
#             "League of legends",
#             "Minecraft"
#         ]
#         print("--Precione 2 para animes")
#         animes = [
#             "Soul Eater",
#             "Fire force",
#             "Bungo straigh dogs",
#             "Persona 5"
#         ]
#         print("--Precione 3 para peliculas")
#         peliculas = [
#             "Sonic",
#             "Jujutsu kaisen 0",
#             "Godzilla minus one",
#             "Shin Godzilla"
#         ]
#         print("--Precione 4 para series")
#         series = [
#             "Centauria",
#             "Flash",
#             "Ninja go",
#             "el ultimo maestro aire"
#         ]
#         print("--Precione 5 para sorpresa")
#         x = int(input())
#         if x == 1:
#             print(juegos)
#         elif x == 2:
#             print(animes)
#         elif x == 3:
#             print(peliculas)
#         elif x == 4:
#             print(series)
#         elif x == 5:
#             os.system("start Brave")
#         else:
#             break
    
    

# menu()





#Prueba 4

# def filtroPares(num):
#     return num % 2 == 0

# numeros = [10,24,5,6,9]


# print(list(filter(filtroPares,numeros)))


#Prueba 5

# def triplicar(numeros):
#     return list(map(lambda x : x * 3, numeros))

# numeros = [2,4,3,6,7,3]

# triplicados = triplicar(numeros)

# print(triplicados)


#prueba 6

