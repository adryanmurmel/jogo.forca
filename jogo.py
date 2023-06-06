import random

palavras = ["primeiro", "Carlos", "jogar", "pizza", "hamburguer"]

random_palavras = random.choice(palavras)
print(random_palavras)
 
x = 5

 if x%2 == 0:
    print("par")
elif x%2 == 1:
    print("impar")

for numero in range(len(palavras)):
    print(palavras[numero])
