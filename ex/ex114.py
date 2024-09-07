import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://felipekauan.vercel.app/')
except:
    print('\033[31mO site do Felipe não está acessível no momento!\033[m')
else:
    print('\033[33mConsegui acessar o site do Pudim com sucesso!\033[m')
    print(site.read())
