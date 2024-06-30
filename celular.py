senhaCadastrada = input("Antes de ligar o celular,  cadastre uma senha: ")

print("\nCelular ligado com sucesso.")

for tentativa in range(3):
    senha = input("Digite a senha: ")
    
    if senha == senhaCadastrada:
        print("Bem-vindo.")
        break
    else:
        tentativas_restantes = 2 - tentativa
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você tem mais {tentativas_restantes} tentativa(s).")
        else:
            print("Telefone bloqueado, tente novamente mais tarde.")
