from random import randint

respostas = {1 : "Sim", 2 : "Não", 3 : "Não sei te dizer"}

def main():
    run = 1
    while run == 1:
        comando = input("-> ")
        if comando != "quit":
            gerarResposta()
        else:
            run = 0

def gerarResposta():
    possibilidade = randint(1, 3)
    print(respostas[possibilidade])

main()