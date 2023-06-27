from random import randint

def duvida(num):
    respostas = {
        1: "Com certeza!",
        2: "É possível.", 
        3: "Por enquanto, não.", 
        4: "Sem chance!", 
        5: "Não conte com isso.", 
        6: "Impossível prever no momento."
    }

    print(f"\n{estilo_texto['negrito']}A resposta do M4g0 é: {cor_texto['verde']}{respostas[num]}{estilo_texto['padrão']}\n")


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

print(f"\n{estilo_texto['negrito']} Faça uma pergunta mentalmente e deixe que o M4g0 das respostas diga sua previsão.{estilo_texto['padrão']}")

while True:
    opcao = str(input(f"Se tiver uma dúvida, aperte [ENTER] para ver a previsão do M4g0.\nOu, digite [0] para encerrar o programa. ")).strip()
    
    if opcao != '0':
        duvida(randint(1, 6))
    elif opcao == '0':
        break

print("PROGRAMA ENCERRADO!")
