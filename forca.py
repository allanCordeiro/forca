import os

palavra_secreta = raw_input("Digite a palavra secreta: ")
os.system("clear")
#agora e fazer a quantidade de tentativas


palavras_tentadas = []
quantidade_de_tentativas = 0
quantidade_palavras_corretas = 0
while quantidade_de_tentativas < 7:
    letra = raw_input("Arrisque sua letra: ")
    if letra in palavras_tentadas:
        print("voce ja tentou a letra [%s]" %letra)
        quantidade_de_tentativas = quantidade_de_tentativas + 0
    else:
        bool_acertou = 0
        for validacao in palavra_secreta:
            if validacao in letra:
                print("miseravi acerto")
                palavras_tentadas.append(letra)
                quantidade_de_tentativas = quantidade_de_tentativas + 0
                quantidade_palavras_corretas=quantidade_palavras_corretas + 1
                #booleano para nao contar a tentativa la embaixo
                bool_acertou = 1
        if quantidade_palavras_corretas == len(palavra_secreta):
            print("Miseravi! Acertou tudo! Parabens!!")
            print("A palavra secreta era: %s" %palavra_secreta)
            break

        else:
            if bool_acertou == 0:
                palavras_tentadas.append(letra)
                quantidade_de_tentativas = quantidade_de_tentativas + 1
                print("Errouuuu!!!")
                if quantidade_de_tentativas == 7:
                    print("Lamento. O jogo acabou pra ti")
