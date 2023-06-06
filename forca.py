import random
from re import

palavras = ["primeiro", "carlos", "jogar", "pizza", "hamburguer", "teclado"]

palavra_escolhida = random.choice(palavras)

print(palavra_escolhida)

print(len(palavra_escolhida))

display = []

for n in range(len(palavra_escolhida)):
    display.append("_")
print(display)

vidas = 6

while vidas >= 0 and "_" in display:
    chute = input("Digite uma letra: ")
    print(chute)
    cont = 0
    acertou = False
    for letra in palavra_escolhida:
        if chute == letra:
            display[cont] = chute
            acertou = True
        cont +=1
    if not acertou:
        vidas -= 1
    print(display)
    print(vidas)
    if "_" not in display:
        print("Você ganhou!!")
        break
    if vidas == 0:
        print("Você perdeu!!\nA palavra era" + random.palavras)
        break
