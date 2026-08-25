print("=======Será que você pode votar?=======")

nome = input("Digite um nome: ")
idade = int(input("Digite um numero: "))

if idade >= 16:
    print(f"Você pode votar {nome}, vote com sabedoria!")
else:
    print(f"Você não pode votar ainda {nome}, espera so mais um pouco...")