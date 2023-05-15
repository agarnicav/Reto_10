# Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

def promedio(lista): # Se define  la funcion para hallar el promedio que recibe como argumento la lista
    suma = 0
    
    for elemento in lista: # Se itera sobre cada elemento de la lista y se van sumando
        suma += elemento
    promedio = suma / len(lista) # Se calcula el promedio dividiendo la suma por la cantidad de elementos en la lista
    return promedio # Se retorna el promedio



if __name__ == "__main__":
    lista = [] # Se crea una lista vacia
    n = int(input("Ingrese el tamaño de la lista: ")) # Se solicita el tamaño de la lista
    for i in range(n):  # se itera Se itera sobre desde cero hasta el tamaño de la lista ingresado por el usuario para ir agregando valores .
        i = float(input("Valores de la lista : ")) # Se solicitan cada valor de la lista 
        lista.append(i) # Se agrega cada valor a la lista
    promedio_lista = promedio(lista) # Se llama a la función promedio
    print("El promedio : " + str(promedio_lista)) # Se imprime el promedio de la lista
