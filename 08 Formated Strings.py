# serve para facilitar a leitura da str e para facilitar a inserção de variáveis

# FRASE: O Mateus Lopes é um excelente [Cientista] de Dados

nome = 'Mateus'
sobrenome = 'Lopes'
profissão = 'Cientista de Dados'

texto1 = f'o {nome} {sobrenome} é um excelente {profissão}'
print(texto1) 

nome = 'Marcos'
sobremesa = 'bolo com sorvete'
dia_semana = 'sábado'

texto2 = f'o {nome} gosta de comer {sobremesa} todo {dia_semana}'
print(texto2)