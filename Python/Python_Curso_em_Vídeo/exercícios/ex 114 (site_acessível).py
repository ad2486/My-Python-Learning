'''
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''
import urllib
import urllib.request
from urllib.error import HTTPError, URLError

try:
    site = urllib.request.urlopen('http://theuselessweb.com')
except (HTTPError, URLError):
    print('Não foi possível acessar o site theuselessweb.com')
else:
    print('O site theuselessweb.com foi acessado com sucesso')
