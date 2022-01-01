from random import randint

def filmes(num):
    perguntas_filmes = {
                1: f'Um {tema} que te inspira.', 
                2: f'Um {tema} para ver com um par romântico.', 
                3: f'O pior {tema} que você já assistiu.', 
                4: f'Seu {tema} favorito de todos os tempos.', 
                5: f'Você busca assistir {tema}s indicados em premiações? Se sim, por quê?', 
                6: f'Prêmios são bons indicadores da qualidade de um {tema}?', 
                7: f'O que você gosta de comer/beber enquanto assiste a um {tema}?', 
                8: f'Qual o tempo de duração aceitável de um {tema}. Quando ele passa a ser longo demais?', 
                9: f'As sequências de um {tema} costumam ser tão boas quanto o original? Dê exemplos de boas sequências, se puder.', 
                10: f'Quais são os seus critérios para decidir que {tema} assistir? O gênero? O diretor? Os atores?', 
                11: f'A violência nos {tema}s incentiva à violência na vida real?', 
                12: f'Um {tema} com uma boa mensagem.', 
                13: f'Um {tema} bom, mas que não veria de novo.', 
                14: f'Um {tema} de que gosta, mas tem vergonha de admitir.', 
                15: f'Um {tema} de que todos gostam, menos você.', 
                16: f'Um {tema} bom pelos motivos errados.', 
                17: f'Um {tema} que é uma boa adaptação de outra mídia (livro, HQ, jogo, música etc).', 
                18: f'Um {tema} nostálgico para você.', 
                19: f'Um bom {tema} de super-herói.', 
                20: f'Um {tema} pelo qual se sente representado.', 
                21: f'Um {tema} que não cansa de assistir.', 
                22: f'Um {tema} que te faz lembrar de alguém.', 
                23: f'Um bom {tema} de drama.', 
                24: f'Um bom {tema} de comédia.', 
                25: f'Um bom {tema} de romance.', 
                26: f'Um bom {tema} de suspense.', 
                27: f'Um bom {tema} de terror.', 
                28: f'Um bom {tema} de ação.', 
                29: f'Um bom {tema} de ficção científica.', 
                30: f'Um bom {tema} em animação.', 
                31: f'Um {tema} que te decepcionou.', 
                32: f'Você desgosta de algum tipo de {tema}? Se sim, qual e por qual motivo?', 
                33: f'Sobre {tema}s baseados em livros: você prefere ler o livro antes ou depois de assistir ao {tema}?', 
                34: f'Um {tema} que você achou muito assustador.', 
                35: f'Um {tema} que você achou muito enfgraçado.', 
                36: f'Um famoso da indústria do cinema que você gostaria de conhecer.', 
                37: 'Um ator de quem você gosta', 
                38: f'Uma atriz de quem você gosta.', 
                39: f'Você acha que {tema} podem desempenhar um papel educacional? Se puder, dê exemplos.', 
                40: f'Um {tema} que você viu recentemente e gostou.', 
                41: f'Você costuma comprar {tema}s?', 
                42: f'Você gostaria de trabalhar com {tema}s?', 
                43: f'Você prefere {tema}s em animação ou em live action?', 
                44: f'Um {tema} com uma boa trilha sonora.', 
                45: f'Na sua opinião, o que é um {tema} clássico?'
                }
    print(f"\n{estilo_texto['negrito']}{cor_texto['ciano']}{perguntas_filmes[num]}{estilo_texto['padrão']}\n")


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

# legenda: \033[STYLE; TEXT; BACKm


tema = 'filme'

while True:

    while True:
        try:
            continuar = int(input(f"Digite: \n[1] para ver a próxima pergunta \n[2] para encerrar o programa \nSua resposta: "))
            break
        except ValueError:
            continue
        
    if continuar == 1:
        filmes(randint(1, 45))
    elif continuar == 2:
        break

print(f"{cor_texto['vermelho']}PROGRAMA ENCERRADO. OBRIGADO PELA PARTICIPAÇÃO!{estilo_texto['padrão']}")