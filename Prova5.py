def calcular_media(notas):
    soma_notas = 0
    quatidade_notas = 0

    for nota in notas:
        soma_notas += nota
        quatidade_notas += 1

    return soma_notas / quatidade_notas if quatidade_notas > 0 else 0

def verificar_situacao(media):
    if media == 10:
        return "Parabéns,sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    

def main():
    nome = input("Digite aqui o seu nome: ")

    notas = []
    num_notas = int(input(f'Digite o número de provas que você teve  {nome}: '))

    for i in range(num_notas):
        nota = float(input(f'Digite a nota {i + 1}  {nome}: '))
        notas.append(nota)

    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    print(f'A sua media {nome} foi de : {media:.2f} E sua situação é: {situacao}')



if __name__ == "__main__":
    main()
