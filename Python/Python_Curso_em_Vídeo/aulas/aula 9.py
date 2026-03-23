frase = 'Curso em Vídeo Python'
#FATIAMENTO
print (frase)
print (frase[9]) #Escreve o caractere de índice 9 da cadeia de caracteres
print (frase[9:13]) #Escreve do caractere 9 até o caractere 12 pois o último é sempre desconsiderado
print (frase[9:21:2]) #Escreve do caractere 9 ao caractere 21 pulando de 2 em 2 
print (frase[:5]) #Escreve do início da cadeia de caracteres até o caractere 4
print (frase[15:]) #Escreve do caractere 15 até o final da cadeia de caracteres
print (frase[9::3]) #Escreve do caractere 9 até o final da cadeia de caracteres pulando de 3 em 3
#ANÁLISE
print (len(frase)) #Escreve o número de caracteres da cadeia de caracteres
print (frase.count('o')) #Escreve o número de vezes que a letra 'o' aparece na cadeia de caracteres
print (frase.count('o', 0,13)) #Escreve o número de vezes que a letra 'o' aparece na cadeia de caracteres do índice 0 ao índice 12
print (frase.find('deo')) #Escreve o índice do início da primeira ocorrência da sequência 'deo' na cadeia de caracteres
print (frase.find('Android')) #Escreve -1 pois a sequência 'Android' não existe na cadeia de caracteres
print ('Curso' in frase) #Escreve True pois a sequência 'Curso' existe na cadeia de caracteres
print ('Android' in frase) #Escreve False pois a sequência 'Android' não existe na cadeia de caracteres
print (frase.lower().find('vídeo')) #Escreve o índice do início da primeira ocorrência da sequência 'vídeo' na cadeia de caracteres, ignorando maiúsculas e minúsculas
#TRANSFORMAÇÃO
print (frase.replace('Python', 'Android')) #Substitui a sequência 'Python' por 'Android' na cadeia de caracteres
print (frase.upper()) #Escreve a cadeia de caracteres em letras maiúsculas
print (frase.lower()) #Escreve a cadeia de caracteres em letras minúsculas
print (frase.capitalize()) #Escreve a cadeia de caracteres com a primeira letra em maiúscula e as demais em minúsculas
print (frase.title()) #Escreve a cadeia de caracteres com a primeira letra de cada palavra em maiúscula e as demais em minúsculas
print (frase.strip()) #Remove os espaços em branco do início e do final da cadeia de caracteres
print (frase.rstrip()) #Remove os espaços em branco do final da cadeia de caracteres
print (frase.lstrip()) #Remove os espaços em branco do início da cadeia de caracteres
frase2 = '   Aprenda Python  '
print (frase2.strip()) #Remove os espaços em branco do início e do final da cadeia de caracteres (agora em prática)
#DIVISÃO
print (frase.split()) #Divide a cadeia de caracteres em uma lista de palavras
print (frase.split()[0]) #Escreve a primeira palavra da cadeia de caracteres
print ('-'.join(frase)) #Une os caracteres da cadeia de caracteres com um traço entre eles
print (''.join(frase)) #Une os caracteres da cadeia de caracteres sem nenhum separador entre eles
dividido = frase.split() #Divide a cadeia de caracteres em uma lista de palavras e armazena na variável 'dividido'
print (dividido[0]) #Escreve a primeira palavra da lista 'dividido'
print (dividido) #Escreve a lista 'dividido' completa, mostrando que a cadeia de caracteres foi dividida em palavras e armazenada na lista
print (dividido[0][3]) #Escreve o caractere de índice 3 da primeira palavra da lista 'dividido' (que é a letra 's' da palavra 'Curso')