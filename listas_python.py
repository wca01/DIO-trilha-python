# exemplo listas
mes = ["janeiro", "fevereiro", "abril"]
print (mes[1])
print (mes[-3])


# exemplo FOR iterar os itens da lista
for item in mes:
    print(item)

# enumerate = saber o indice da lista
for indice, item in enumerate(mes):
    print(f"{indice}: {item}")

# filtros
numeros = [1, 2, 3, 4, 21, 32, 46, 76]
pares = []
for numero in numeros:
    if numero %2 == 0:
        pares.append(numero) #adiciona novos valores a lista

# forma 2 inline
pares2 = [numero for numero in numeros if numero % 2 == 0] 

print (pares, pares2)

#modificando valores v.1
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

#modificando valores v.2
quadrado2 = [numero ** 2 for numero in numeros]
 
print (quadrado, quadrado2)

#metodos da classe list
lista = []

lista.append(1)
lista.append("py")
lista.append([40,50,100])

print(lista)
lista2 = lista.copy() #copia a lista

lista.clear() #limpar lista

print(lista)

#count = contar quantas vezes objeto aparece na lista
lista.count("40")
lista2.count("40")

print(lista2)

#Extend = juntar listas
lista2.extend(["item1", "item2"])
print(lista2)

#index
lista2.index("py") # 1

#pop = pilha de elementos, tira último item da lista, indica com número do índice (0, 1, 2 etc)
lista2.pop()
print("pop", lista2)

#remove = indica o item a remover
lista2.remove("item1")
print("remove", lista2)

#reverse = inverte lista, como tecnica do slice (-1)
lista.reverse()

#sort = ordenar
lista.sort()
lista.sort(reverse=True) # inverte a ordem
lista.sort(key=lambda x:len(x)) # usando ordenação por tamanho de caracteres
lista.sort(key=lambda x:len(x), reverse=True) #ordena por tamanho e inverte

#len = tamanho da lista
len(lista2)

#sorted = função builtin, ordenar listas
sorted(lista, key=lambda x: len(x))