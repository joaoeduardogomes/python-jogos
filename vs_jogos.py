from random import randrange

jogos = [
        "The Last of Us",
        "The Last of US Part II",
        "Life is Strange",
        "Firewatch",
        "Persona 5",
        "Breath of the Wild",
        "It Takes Two",
        "God of War",
        "Pokémon Soul Silver",
        "The Witcher 3",
        "Grim Fandango",
        "Tales From The Borderlands"
    ]


while len(jogos) > 1:

    a = randrange(0, len(jogos))

    b = randrange(0, len(jogos))
    if b == a:
        while b == a:
            b = randrange(0, len(jogos))
        
    print(f"\n")
    print(f"{jogos[a]} vs {jogos[b]}")

    while True:
        try:
            escolha = int(input("Qual dos dois você prefere? "))
            break
        except ValueError:
            continue
    if escolha == 1:
        jogos.pop(b)
    elif escolha == 2:
        jogos.pop(a)

    print(jogos)


print(f"O vencedor é: {jogos}")