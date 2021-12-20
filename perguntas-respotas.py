from random import randint

def filmes(num):
    perguntas_filmes = {1: f'Um {tema} que te inspira.', 
                2: f'Um {tema} para ver com um par romântico.', 
                3: f'O pior {tema} que você já assistiu.', 
                4: f'Seu {tema} favorito de todos os tempos.', 
                5: f'você busca assistir {tema}s indicados a premiações? Se sim, por quê?', 
                6: f'Prêmios são bons indicadores da qualidade de um {tema}', 
                7: f'O que você gosta de comer enquanto assiste a um {tema}?', 
                8: f'Qual o tempo de duração aceitável de um {tema}. Quando ele passa a ser longo demais?', 
                9: f'As sequências de um {tema} costumam ser tão boas quanto o original? Dê exemplos de boas sequências, se puder.', 
                10: f'Quais são os seus critérios para decidir que {tema} assistir? O gênero? O diretor? Os atores?', 
                11: f'A violência nos {tema}s inspiram violência na vida real?', 
                }
    print(perguntas_filmes[num])

tema = 'filme'
filmes(randint(1, 11))