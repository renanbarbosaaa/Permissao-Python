nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
altura = float(input("Digite a altura da pessoa (em metros): "))


resultado = idade >= 18 and altura >= 1.75


msg = "Pode participar do evento? " + str(resultado)


print(msg)