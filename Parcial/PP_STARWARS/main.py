'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones
from funciones import cargar_json, listar_por_altura,mostrar_personaje_mas_alto,ordenar_personajes_peso,exportar_csv,buscador_personaje
import json
import re

ubicacion = r"C:\Users\facun\OneDrive\Escritorio\Parcial\PP_STARWARS\data.json"

def starwars_app():
    lista_personajes = funciones.cargar_json(ubicacion)
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            print("1 - Listar los personajes ordenados por altura\n")
            Listado = listar_por_altura(lista_personajes)
            print(Listado)
        elif(respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            mostrar_personaje_mas_alto(lista_personajes)
        elif(respuesta=="3"):
            print("3 - Ordenar los personajes por peso\n")
            Listado_peso = ordenar_personajes_peso(lista_personajes)
            print(Listado_peso)
        elif(respuesta=="4"):
            genero = input("4 - Ingrese el genero del personaje a buscar: \n")
            buscador_personaje(lista_personajes,genero)
        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")
            exportar_csv(lista_personajes,"path")
        elif(respuesta=="6"):
            break


starwars_app()

