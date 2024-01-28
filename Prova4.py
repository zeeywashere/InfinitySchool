velocidade = float(input("QUal a velocidade do seu carro: "))
limite_velocidade = 80
aplicacao_multa = velocidade - limite_velocidade
multa = aplicacao_multa *20

if velocidade > 80:
    print(f"Sua velocidade está muito alta, estarei aplicando a multa de {multa} ")


    
else:
    print('Ta liberado')





   