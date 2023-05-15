# Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.


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