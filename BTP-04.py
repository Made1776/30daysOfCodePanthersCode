def sumar_numeros_pares(limite_inferior, limite_superior):
    return sum(numero for numero in range(limite_inferior, limite_superior + 1) if numero % 2 == 0)

def main():
    casos = int(input("Ingrese la cantidad de casos: "))

    for _ in range(casos):
        limite_inferior, limite_superior = map(int, input("Ingrese el rango (ejemplo: 1-10): ").split('-'))
        suma_pares = sumar_numeros_pares(limite_inferior, limite_superior)
        print("La suma de los números pares es:", suma_pares)

main()
