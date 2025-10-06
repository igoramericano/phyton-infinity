def calcular_media(notas):
    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f'A média é {media:.2f}')
    else:
        print('Nota não registrada')
