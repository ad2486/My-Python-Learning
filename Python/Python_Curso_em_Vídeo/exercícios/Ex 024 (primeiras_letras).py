nome = input('Digite o nome da cidade:').strip()
cidade = nome.split()
cidadeMaiúscula = cidade[0].upper()
if 'SANTO' in cidadeMaiúscula:
    print('A primeira palavra do nome da cidade é Santo!')
else:    print('A primeira palavra do nome da cidade não é Santo!')
