import requests

def verificação(msg):
    try:
        requests.get(msg)
    except Exception as error:
        print(f'\033[31mO SITE "pudim.com.br" NÃO ESTÁ ACESSÍVEL!!!\033[m')
    else:
        print(f'\033[33mO SITE "pudim.com.br" ESTÁ ACESSÍVEL!\033[m')

verificação('http://www.pudim.com.br')