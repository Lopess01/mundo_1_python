#               MANIPULANDO STRINGS

''' o fatiamento consiste em recortar a string e utilizar 
os blocos na memória para manipular. obs: no fatiamento
é utilizado os [] por que são uma lista de caracteres
começando em 0'''

frase = 'curso em vídeo python'
frase[9]
# nesse caso eu peguei apenas o caracter 9, que retorna o V

frase[9:13]
# quando eu utilizo o : eu fatio uma parte da frasen nesse caso
# eu peguei do caracter 9 ao 13. Obs: o 13 não é mostrado, então
# só vai até o 12.

frase[9:21:2]
# após  eu adicionar mais um :, irá ser printado a frase do
# 9 até o 21, pulando de dois em dois caracteres retornando apenas
#vdopto

frase[:5]
frase[5:]
frase[9::3]
#quando não há nenhum valor antes ou após o :, significa que vai
# ser mostrado todos os caracteres que vem antes ou depois, e 
# quando está entre os dois pontos ele vai ir até o final a partir
# do 9 pulando de 3 em 3

len(frase)
# o len é utilizado pra medir o tamanho da frase, lembrando que 
# começa em 0

frase.count('o')
# o count é utilizado pra contar quantas strings possuem esse valor
# dentro da frase

frase.count('o', 0 ,13)
# nesse caso eu pedi pro python contar quantas vezes existe o 
# 'o' do 0 ao 13

frase.find('deo')
print(frase.find('carai de asa'))
# o find busca o termo dentro do parametro e indica a posicão 
# que ele começa, e quadno não é encontrado nada ele retorna
# -1 no terminal

print('curso' in frase)
# o in é utilizado para verificar se há ou não a strong dentro 
# da frase, ele retorna apenas True or False

x = frase.replace('python', 'R')
print(x)
# o replace substitui os termos colocadosn nesse caso, o python
# foi substituido pelo R

frase.upper()
frase.lower()
frase.title()
frase.capitalize()
frase.title()
# essas quatro funções manipulam deixando elas maiusculas(upper),
# minusculas(lower), deixa a primeira letra da frase em maiusculo,
# (captalize), e deixam todas as primeiras letras maiusculas(title).

frase = '   aprenda python   '

frase.strip()
frase.rstrip()
frase.lstrip()
# o strip remove todos os espaços que vem antes e depois da frase,
# o que vem entre as palavras não é retirado, quando se põe o r ou
# o L antes, ele remove apenas da direita ou da esquerda
 
frase.split()
# o split reparte as palabvras que estão entre os espaços
# dividindo em listas diferentes

' '.join(frase)
# o join adiciona e junta a frase separada com o termo colocado
# entre as aspas


