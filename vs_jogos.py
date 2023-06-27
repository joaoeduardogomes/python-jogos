from random import randrange
from time import sleep

def importa_jogos():
    arquivo = open("vs_jogos.txt", encoding = 'utf-8', mode = "r")

    global jogos
    jogos = []

    for linha in arquivo:
        linha = linha.strip()
        jogos.append(linha.title())
    
    arquivo.close()

def mostra_mensagem():
    mensagem = "Bem-vindo(a) ao Battle Royale dos jogos!"
    tamanho = len(mensagem) + 4
    print("*" * tamanho)
    print(f"  {mensagem}")
    print("*" * tamanho)

    criterios = ['jogabilidade', 'história', 'narrativa', 'construção de mundo', 'gráfico']

    print(f"O critério é: {criterios[randrange(0, len(criterios))]}")
    sleep(1)


estilo_texto = {'padrão':'\033[0m',
        'negrito' : '\033[1m', 
        'sublinhado':'\033[4m',
        'invertido':'\033[7m',}

cor_texto = {'limpa':'\033[m',
        'branco' : '\033[30m', 
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'ciano' : '\033[36m', 
        'cinza' : '\033[37'}

cor_fundo = { 'branco' : '\033[40m', 
        'vermelho':'\033[41m',
        'verde':'\033[42m',
        'amarelo':'\033[43m',
        'azul':'\033[44m',
        'roxo':'\033[45m',
        'ciano' : '\033[46m', 
        'cinza' : '\033[47'}

"""jogos = [
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
    ]"""

importa_jogos()
print(f"\n")
mostra_mensagem()

while len(jogos) > 1:
    print(f"\n Participam deste rodada: \n")
    print(jogos)

    a = randrange(0, len(jogos))

    b = randrange(0, len(jogos))
    if b == a:
        while b == a:
            b = randrange(0, len(jogos))
        
    print(f"""
        {estilo_texto['negrito']}{cor_texto['ciano']}
        {jogos[a]}
        {cor_texto['limpa']} 
        vs 
        {estilo_texto['negrito']}{cor_texto['amarelo']}
        {jogos[b]}
        {cor_texto['limpa']}
        """)

    while True:
        try:
            escolha = int(input("Qual dos dois você prefere? "))
            break
        except ValueError:
            continue
    if escolha == 1:
        print(f"""{cor_texto['vermelho']}
        {jogos[b]} foi eliminado! 
        {cor_texto['limpa']}""")
        jogos.pop(b)
    elif escolha == 2:
        print(f"""{cor_texto['vermelho']}
        {jogos[a]} foi eliminado!
        {cor_texto['limpa']}""")
        jogos.pop(a)
    sleep(1)


print(f"O vencedor é: {estilo_texto['negrito']}{cor_texto['verde']}{jogos}{cor_texto['limpa']}")