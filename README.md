# Primer punto 
Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

## Codigo: 
           
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
        
        
       
# Segundo punto
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

## Codigo: 

    def producto_punto(lista1, lista2):
        if len(lista1) != len(lista2): # se verifica que las listas tengan el mismo tamaño
            return 0
        producto_punto = 0 # se inicializa el valor del producto punto en 0
        for i in range(len(lista1)): # se itera sobre las dos listas al mismo tiempo
           producto_punto += lista1[i] * lista2[i] # se calcula el producto de los elementos de las dos listas y se suman
        return producto_punto # se retorna el valor final del producto punto


    if __name__ == "__main__":
        lista1 = [] # Se crea una lista vacia
        lista2 = [] # Se crea una lista vacia
        n = int(input("Ingrese el tamaño de la listas : ")) # Se solicita el tamaño de la lista
        for i in range(n): # se itera Se itera sobre desde cero hasta el tamaño de la lista 1  ingresado para ir agregando valores .
            i = float(input("Valores de la lista 1 :")) # Se solicitan cada valor de la lista 1
        for j in range(n): # se itera Se itera sobre desde cero hasta el tamaño de la lista 2 ingresado para ir agregando valores .
            j = float(input("Valores de la lista 2 : ")) # Se solicitan cada valor de la lista 2
            lista1.append(i) # Se agrega cada valor a la lista 1
            lista2.append(i) # Se agrega cada valor a la lista 1
        produccto_punto_listas = producto_punto(lista1, lista2) # Se llama a la función producto punto
    
        print("El producto : " + str(produccto_punto_listas)) # Se imprime el pruducto punto de la listas


# Tercer punto
Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

## Codigo: 

    def ceros_al_final(lista):  # Se define la función que toma como a lista como argumento
        lista_sin_ceros = []  # lista vacia para almacenar los elementos distintos de cero de la lista original
        ceros = []  # lista vacia para almacenar los ceros encontrados en la lista original
        for elemento in lista: 
            if elemento != 0:  # Se Buscan los elementos distintos de cero
                lista_sin_ceros.append(elemento) # se agrega el elemento a la lista_sin_ceros si es distinto de cero
            else:
                ceros.append(elemento) # se agrega el elemento a la lista ceros si es cero
        lista_sin_ceros.append(ceros) # se agrega la lista de ceros al final de la lista_sin_ceros
        return lista_sin_ceros 

    if __name__ == "__main__":
        lista = [] # Se crea una lista vacia
        n = int(input("Ingrese el tamaño de la lista: ")) # Se solicita el tamaño de la lista
        for i in range(n):  # se itera Se itera sobre desde cero hasta el tamaño de la lista ingresado por el usuario para ir agregando valores .
            i = float(input("Valores de la lista : ")) # Se solicitan cada valor de la lista 
            lista.append(i) # Se agrega cada valor a la lista

        ceros_ = ceros_al_final(lista) # Se llama a la función ceros_al_final
        print(" la lista ingresada es " +str(lista)) # se imprime la lista ingresada al principio para poder apreciar los cambios
        print("la lista agregando los ceros encontrados al final es : " + str(ceros_)) # Se imprime el promedio de la lista
        
        
# Cuarto punto 
Algoritmos de sorting: Un algoritmo de sorting, proceso  que organiza elementos de una lista en un orden específico. El orden puede ser ascendente o descendente, y pueden ser objetos, números y letras.

Bubble Sort: este es el algoritmo de sorting más simple, pero también el menos eficiente. Funciona comparando elementos adyacentes y intercambiándolos si están en el orden incorrecto. El proceso se repite hasta que la lista esté ordenada. 
