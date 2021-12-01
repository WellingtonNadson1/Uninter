# Solicitar o nome do usuário
nome = input('Digite um Nome: ')

# Transformando o nome do 
# usuário para maiusculas
nome_upper = nome.upper()

# Criando um dicionário para as 
# vogais e seus correspondentes
vogais = {
    "A" : "@",
    "E" : "&",
    "I" : "!",
    "O" : "#",
    "U" : "*"
}

# Criando um loop para verificar 
# as presenças das vogais constantes no dicionário que
# estejam presentes no nome digitado pelo usuário e 
# fazendo o replace nas que estiverem presentes.
for v in vogais:
    nome_upper = nome_upper.replace(v, vogais[v])
print(nome_upper)
