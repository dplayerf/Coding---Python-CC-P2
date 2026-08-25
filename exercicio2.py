print("=======Tabuada=======")

num = int(input("Digite um numero: "))
print("-" * 12)

for banana in range(1,10 + 1):
    resul = num * banana
    print(f"{num:2} X {banana:2} = {resul}")

print("-" * 12)