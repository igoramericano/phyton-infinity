import urllib
import urllib.request

try:
    site= urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu Erro')
else:
    print('Consegui acessar o site com sucesso')