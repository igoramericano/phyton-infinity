def calcular_estatisticas_simples(*numeros):
    return {
        'quantidade': len(numeros),
        'soma': sum(numeros),
        'média': sum(numeros) / len(numeros),
        'maior': max(numeros),
        'menor': min(numeros)
    }
    
resultado = calcular_estatisticas_simples(10, 5, 8, 15, 2)
print(resultado)

resultado2 = calcular_estatisticas_simples(7, 7, 7)
print(resultado2)