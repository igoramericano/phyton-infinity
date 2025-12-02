from datetime import date

# Pede ao usuário para digitar um ano.
# A mensagem informa que digitar 0 analisará o ano atual.
ano = int(input('Digite o ano que quer analisar (ou digite 0 para analisar o ano atual): '))

# Se o usuário digitou 0, a variável 'ano' recebe o ano atual.
if ano == 0:
    ano = date.today().year

# Verifica as condições para um ano ser bissexto:
# 1. É divisível por 4, mas não por 100.
# 2. OU é divisível por 400.
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))