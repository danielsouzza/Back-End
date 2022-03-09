from socket import gethostbyname as conect


url = input("Digite um site:")
try:
    conect(url)
    print("\033[1;36mO site está acessível")
except:
     print("\033[0;31mO site não está acessível")