def cumprimento(texto):
    return f"Olá, {texto}"

print(cumprimento("Laura da Cruz Barbosa"))


import random

def media_sete_numeros():
    numeros = [random.randint(1, 100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    print("Números sorteados:", numeros)
    return media

print("Média dos 7 números:", media_sete_numeros())
