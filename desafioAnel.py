entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])


comunicacao = distancia / (diametro1+diametro2)

print("%.2f" %comunicacao)

entrada = input().split()

tempo = int(entrada[0])
velocidade = int(entrada[1])

consumo = (tempo*velocidade)/12

print("%.3f" %consumo)