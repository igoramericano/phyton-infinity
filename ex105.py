def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'APROVADO'
        elif r['Média'] < 7 and r['Média'] >= 5:
            r['Situação'] = 'RECUPERAÇÃO'
        else:
            r['Situação'] = 'REPROVADO'
    print(f'{r}')
     
#programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)