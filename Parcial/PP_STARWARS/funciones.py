import json
import re




def cargar_json(path:str)->list:
    with open(path, "r") as file:
        buffer = json.load(file) #En el buffer se va a almacenar la cargar del archivo, en este caso "file"
        return buffer["results"] #Retornamos  la lista.


 
def listar_por_altura(lista_heroe:list) -> list:
    lista_duplicada = lista_heroe.copy()
    flag_swap = True
    maximo_heroes = len(lista_heroe)
    hasta = 1

    while flag_swap == True:
        flag_swap = False
        for i in range(maximo_heroes -hasta):
            if lista_duplicada[i]["height"] > lista_duplicada[i+1]["height"]:
                lista_duplicada[i], lista_duplicada[i+1] = lista_duplicada[i+1], lista_duplicada[i] #Swapeamos
                flag_swap = True
    hasta += 1
    return lista_duplicada

def mostrar_personaje_mas_alto(lista_heroe:list) -> list: 
  lista_duplicada = lista_heroe.copy()
  lista_fem = []
  lista_masc = []

  for heroe in lista_heroe:
      if re.search("female",heroe["gender"],re.IGNORECASE):
          lista_fem.append(heroe)
      elif re.search("male",heroe["gender"],re.IGNORECASE):  
          lista_masc.append(heroe)
  mas_alto_fem = listar_por_altura(lista_fem) #Se saca provecho de la funcion listar por altura para que ordene la lista de mayor a menor.
  mas_alto_masc = listar_por_altura(lista_masc)
  print(mas_alto_fem[0])
  print(mas_alto_masc[0])

def ordenar_personajes_peso(lista_heroes:list) -> list:
    lista_duplicada = lista_heroes.copy() # Duplicamos la lista para no alterar la lista original.
    flag_swap = True #Utilizamos el flag para saber cuando esta la lista ordenada finalmente.
    maximo_heroes = len(lista_heroes)
    hasta = 1 #Hasta es el delimitador de vueltas.

    while flag_swap == True:
        flag_swap = False
        for i in range(maximo_heroes -hasta):
            if lista_duplicada[i]["mass"] < lista_duplicada[i+1]["mass"]:
                lista_duplicada[i], lista_duplicada[i+1] = lista_duplicada[i+1], lista_duplicada[i] 
                flag_swap = True
    hasta += 1
    return lista_duplicada


def buscador_personaje(lista_heroe:list, genero:str)->list: #Buscador por genero
    lista_duplicada = lista_heroe.copy()
    lista_nueva = []

    while genero != "male" and genero != "masc" and genero != "n/a":
        genero = input("Error: Ingrese correctamente el genero (male/masc/n/a):\n")

    if genero == "male":
         for heroe in lista_duplicada:
             if re.search("male",heroe["gender"],re.IGNORECASE):
                 lista_nueva.append(heroe)
    elif genero == "masc":
         if re.search("masc",heroe["gender"],re.IGNORECASE):
              lista_nueva.append(heroe)
    elif genero == "n/a":
         if re.search("n/a",heroe["gender"],re.IGNORECASE):
              lista_nueva.append(heroe)
    
    print(lista_nueva)
    return(lista_nueva)


    


def exportar_csv(lista_personajes:list,path:str):
    with open("w+") as file: #Abrimos el archivo en modo escritura
        for elemento in lista_personajes: #Iteramos todos los elementos de la lista personjes
            file.write("{0} - {1} - {2} - {3}".format(elemento["name"], elemento["height"],elemento["mass"],elemento["gender"])) # Escribimos en el archivo creado anteriormente.








      
 

        








 
 
 
 
 

        

           
 

 








 
           



