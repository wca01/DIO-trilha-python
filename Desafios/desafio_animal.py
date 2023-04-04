# ''' 
# IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
#  - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
#    casos, é necessário converter/tratar os dados de entrada; 
#  - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#    impressão dos dados de saída. 
# '''
# a = input() 
# b = input() 
# c = input() 

# if a == 'vertebrado' and b == 'ave':
#     if c=='carnivoro':
#         print('aguia')
#     if c=='onivoro':
#          print('pombo')
# elif a == 'vertebrado' and b == 'mamifero':
#     if c=='onivoro':
#         print('homem')
#     if c=='herbivoro':
#         print('vaca')
# elif a == 'invertebrado' and b=='inseto':
#     if c=='hematofago':
#         print('pulga')
#     if c=='herbivoro':
#         print('lagarta')
# elif a == 'invertebrado' and b =='anelideo':
#     if c=='hematofago':
#         print('sanguessuga')
#     if c=='onivoro':
#         print('minhoca')

# Respota aceita abaixo. Acima meu codigo.
A = input()
B = input()
C = input()

if A == 'vertebrado' and B == 'ave' and C == 'carnivoro':
  resposta = 'aguia'

if A == 'vertebrado' and B == 'ave' and C == 'onivoro':
  resposta = 'pomba'

if A == 'vertebrado' and B == 'mamifero' and C == 'onivoro':
  resposta = 'homem'

if A == 'vertebrado' and B == 'mamifero' and C == 'herbivoro':
  resposta = 'vaca'

if A == 'invertebrado' and B == 'inseto' and C == 'hematofago':
  resposta = 'pulga'

if A == 'invertebrado' and B == 'inseto' and C == 'herbivoro':
  resposta = 'lagarta'

if A == 'invertebrado' and B == 'anelideo' and C == 'hematofago':
  resposta = 'sanguessuga'

if A == 'invertebrado' and B == 'anelideo' and C == 'onivoro':
  resposta = 'minhoca'

print(resposta)