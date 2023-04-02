#para tirar informação de uma Str, Int ou float sem precisar pegar a informação completa
fruta = 'abacate'
 #Index 0123456
#cada caracter (letras da palavra abacate) é um index (posição 0= letra A, POSIÇÃO 1 = LETRA b ETC)
print(fruta[3])
print(fruta[4])
print(fruta[2:5]) #colocar sempre 1 valor a mais pois ele come o último index
print(fruta[2:6])

valor = 99.75
#Index 01234 (obs: ponto e vírgula conta como index)
valor = str(valor)

print(valor[2:5])