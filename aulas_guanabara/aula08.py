#UTILIZANDO MÓDULOS
import random
import math
import emoji
# o import serve para trazer uma biblioteca que não está no python cru 
# para o código

from math import sqrt
#o from é utilizado pra trazer apenas uma função da biblioteca para o 
#código 

'''funções do math'''
n = 5.23
print(math.sqrt(n))
# quando o from é utilizado, não é preciso do math. antes da função
print(sqrt(n))

print(math.ceil(n))
print(math.floor(n))
# o ceil arrendonda pra cima e o floor pra baixo

n = random.random()
# agora não estamos mais na biblioteca math, importei o random e essa 
# função gera um número aleatório de 0 a 1

n = random.randint(1,8)
print(n)
# o randint gera um número aleatorio dentro da range dos dois números 
# adicionados entre ()

emo = emoji.emojize('python is :thumbs_up:')
print(emo)
#importei uma biblioteca chaamda emoji, é meio autoexplicativo, mas 
# estou mostrando a utilizade dos módulos em python

mo = emoji.emojize('Hello World :globe_showing_Americas: !', )
print(mo)
#busque sempre na documentação caso não queira erros no codigo