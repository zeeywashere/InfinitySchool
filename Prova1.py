pares = []
impares = []

for i in range (10):
	num = int (input (F'Digite o {i+1} número: '))
	
	if num % 2 == 0: 
		pares.append(num)
	else:
		impares.append(num)

print (F'\na quantidade de números pares é: {len(pares)}. \nOs números pares são {pares}. \nA soma entre eles é {sum(pares)}.')
print (F'\nA quantidade de números ímpares é: {len(impares)}. \nOs números ímpares são {impares}. \nA soma entre eles é {sum(impares)}.')