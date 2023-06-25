def generar_espiral(n):
    # Crear una matriz vacía de tamaño n x n
    matriz = [[0] * n for _ in range(n)]
    
    # Definir los límites superior, inferior, izquierdo y derecho de la matriz
    limite_superior, limite_inferior = 0, n - 1
    limite_izquierdo, limite_derecho = 0, n - 1
    
    # Inicializar el número actual y la dirección inicial (derecha)
    numero_actual = 1
    direccion = "derecha"
    
    # Rellenar la matriz en espiral
    while limite_superior <= limite_inferior and limite_izquierdo <= limite_derecho:
        if direccion == "derecha":
            for i in range(limite_izquierdo, limite_derecho + 1):
                matriz[limite_superior][i] = numero_actual
                numero_actual += 1
            limite_superior += 1
            direccion = "abajo"
            
        elif direccion == "abajo":
            for i in range(limite_superior, limite_inferior + 1):
                matriz[i][limite_derecho] = numero_actual
                numero_actual += 1
            limite_derecho -= 1
            direccion = "izquierda"
            
        elif direccion == "izquierda":
            for i in range(limite_derecho, limite_izquierdo - 1, -1):
                matriz[limite_inferior][i] = numero_actual
                numero_actual += 1
            limite_inferior -= 1
            direccion = "arriba"
            
        elif direccion == "arriba":
            for i in range(limite_inferior, limite_superior - 1, -1):
                matriz[i][limite_izquierdo] = numero_actual
                numero_actual += 1
            limite_izquierdo += 1
            direccion = "derecha"
    
    return matriz

# Solicitar al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))

# Generar la matriz en espiral
matriz_espiral = generar_espiral(n)

# Imprimir la matriz en espiral
for fila in matriz_espiral:
    print("\t".join(map(str, fila)))
