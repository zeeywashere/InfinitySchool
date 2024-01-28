# Numeros inteiros
#Exemplo:
Numero = 99

# Float (Numeros Flutuantes)
#Exemplo:
saldo = 3.53

# String (Cadeia de caracteres)
#Exemplo:
nome = 'Huan'

# Boleano (Verdadeiro ou falso)
#Exemplo:
tem_carro = True

# Solitação de dados de usuarios
nome = input("Digite aqui o seu nome: ")
idade = int(input(f'Ok {nome} agora me diga quantos anos você tem: '))
altura = float(input(f'Digite sua altura {nome}: '))

# Mensagem que irá aparecer:

print('\nInformações fornecidas pelo usuario são: ')
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Altura {altura} metros')