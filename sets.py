# set coleção de objetos não repetidos
numeros = set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
letras = set ("abacaxi") # {'i', 'a', 'b', 'x', 'c'}
carros = set(("palio", "gol", "celta", "palio")) # {'celta', 'palio', 'gol'}

# não retonar em ordem os dados
print(numeros)
print(letras)
print(carros)

# Acessando os dados
# precisa converter para lista
lnumeros = list(numeros)

# Iterar
for carro in carros:
    print(carro)
# gol
# celta
# palio

# enumerar
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
# 0: gol
# 1: celta
# 2: palio





