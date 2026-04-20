'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
palavras = (
    "Abacaxi", "Esferografica", "Sol", "Paralelepipedo", 
    "Python", "CMPA", "Algoritmo", "UFRGS", "Basquete", 
    "Microscopio", "Zsh", "Configuraçao", "Monitor", 
    "Desenvolvimento", "Fisica", "Ressonancia"
)
vogais = (
    'a', 'e', 'i', 'o', 'u'
) 
for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos:", end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra.lower(), end='')
    
