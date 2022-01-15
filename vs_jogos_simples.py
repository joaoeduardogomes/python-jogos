from random import randint
from random import shuffle

jogos = {
        1: "The Last of Us",
        2: "The Last of US Part II",
        3: "Life is Strange",
        4: "Firewatch",
        5: "Persona 5",
        6: "Breath of the Wild",
        7: "It Takes Two",
        8: "God of War",
        9: "Pokémon Soul Silver",
        10: "The Witcher 3",
        11: "Grim Fandango",
        12: "Tales From The Borderlands"
        }


while True:

    a = 0
    b = 0

    while a not in jogos.keys():
        a = randint(1, len(jogos))

    while (b not in jogos.keys()) or (b == a):
        b = randint(1, len(jogos))
        
    print(f"\n")
    print(f"{jogos[a]} vs {jogos[b]}")

    while True:
        try:
            escolha = int(input("Qual dos dois você prefere? "))
            break
        except ValueError:
            continue
    if escolha == 1:
        del jogos[b]
    elif escolha == 2:
        del jogos[a]

    if len(jogos) == 1:
        break
    print(jogos)

print(f"O vencedor é: {jogos}")