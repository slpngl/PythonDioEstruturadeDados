frutas = ["laranja", "maca", "uva", "pera","maça"]
print(frutas)
print(frutas[0])
print(frutas[2])
print(frutas[-1])
#pega o ultimo elemento, podendo-se trabalhar com -


letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

##MATRIZ

matriz = [
    [1 , "A", 2],
    ["b", 3, 4],
    [5 ,"x" ,6]
]

print(matriz[0])  
print(matriz[0][0])  
print(matriz[0][-1]) 
print(matriz[-1][-1]) 

###FATIAMENTO
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

## Percorrendo listas
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

##enumerate 

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

## Compreensão de Listas (tipo um filtro) e modificação dos eleme4ntos

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
