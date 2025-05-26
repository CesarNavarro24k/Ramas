def calcular_promedio(lista):
    suma = 0
    for i in range(0, len(lista)):
        suma += lista[i]
    promedio = suma / len(lista)
    return promedio

notas = [3.5, 4.0, 2.5,5.0,1.0] # 3.3
print("El promedio es:", calcular_promedio(notas))

