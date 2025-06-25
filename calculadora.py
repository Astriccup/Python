def calculadora():
    operacao = input("Digite a operação (+, -, *, /): ")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro: Divisão por zero!"
            else:
                resultado = num1 / num2
        else:
            resultado = "Operação inválida!"

        print(f"O resultado da operação {operacao} é: {resultado}")
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

calculadora()