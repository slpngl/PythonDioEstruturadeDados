def exibir_mensagem():
    print("Hello World")

def exibir_mensagem1(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem2(nome= "Anonymus"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()

def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([10,20,30]))

def retorna_aes(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor

print(retorna_aes(10))

