# Dicionário com nomes das contas e suas senhas
senhas = {
    "gmail": "senha_do_gmail123",
    "github": "senha_do_github456",
    "netflix": "senha_netflix789"
}

# Exibe as contas disponíveis
print("Contas disponíveis:", ", ".join(senhas.keys()))

# Solicita ao usuário o nome do site
site = input("Digite o nome do site: ").lower()

# Verifica se o site existe no dicionário
if site in senhas:
    print(f"A senha para o site '{site}' é: {senhas[site]}")
else:
    print(f"Senha não encontrada para o site '{site}'.")