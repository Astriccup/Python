import random

numero_secreto = random.randint(20, 50)
tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
    try:
        chute = int(input(f"Tentativa {tentativas + 1} de {max_tentativas} - Digite um número entre 20 e 50: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if chute < 20 or chute > 50:
        print("Número fora do intervalo permitido.")
        continue

    tentativas += 1

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif chute > numero_secreto:
        print("O número secreto é MENOR que o seu chute.")
    else:
        print("O número secreto é MAIOR que o seu chute.")

if chute != numero_secreto:
    print(f"Você não conseguiu adivinhar o número secreto. Era {numero_secreto}.")