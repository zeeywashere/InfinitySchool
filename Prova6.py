email = "huhulindo@gmail.com"
senha = "huhulindo123"

while True:
    
    b1 = input("Digite seu email: ")
    b2 = input("DIgite sua senha: ")
    
    if b1==email and b2==senha:
        print("Login realizado com sucesso !")
        break
    else:
        print("Usuario ou a senha incorreta, tente novamente !")