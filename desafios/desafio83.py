#validando expressões regulares

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr: #for transforma a string em uma lista
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: #se o tamanho da pilha for maior que 0, remova o ultimo elemento
            pilha.pop(-1)
        else:
            pilha.append(')') #se a pilha tiver vazia, adicione um ' ) '
            break