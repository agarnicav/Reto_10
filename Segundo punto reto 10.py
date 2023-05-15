# Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

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
