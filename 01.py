def calculadora():
    print("Calculadora \n")
    print("Escolha a operação:")
    print("1 - para Adição (+)")
    print("2 - para Subtração (-)")
    print("3 - para Multiplicação (*)")
    print("4 - para Divisão (/)\n")

   
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    numero1 = float(input("Digite o primeiro número: "))

    numero2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = numero1 + numero2
        print(f"Resultado: {numero1} + {numero2} = {resultado}")
    elif escolha == '2':
        resultado = numero1 - numero2
        print(f"Resultado: {numero1} - {numero2} = {resultado}")
    elif escolha == '3':
        resultado = numero1 * numero2
        print(f"Resultado: {numero1} * {numero2} = {resultado}")
    elif escolha == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado: {numero1} / {numero2} = {resultado}")
    else:
        print("Erro: ao escolher a operação!")

while True:
    calculadora()
    resultado = input("Deseja realizar mais alguma operação sim - s| não - n").lower()
    if resultado  == "s":
        calculadora()
    else:
        break
        
    