from random import randint

jogos = {
        1: "The Last of Us",
        2: "The Last of US Part II",
        3: "Life is Strange",
        4: "Firewatch",
        5: "Persona 5",
        6: "Breath of the Wild",
        7: "It Takes Two",
        9: "Pokémon Soul Silver",
        10: "The Witcher 3",
        11: "Grim Fandango",
        12: "Tales From The Borderlands"
        }


a = randint(1, len(jogos))
b = randint(1, len(jogos))
print(f"\n")
print(f"{jogos[a]} vs {jogos[b]}")


# Finalistas
lista = ["Limbo", "Journey", "Rain"]
numeros = [1, 2, 3]
dicionario = dict(zip(numeros, lista))
print(dicionario)

num = []
for i in range(1, len(lista)+1):
    num.append(i)
print(num)