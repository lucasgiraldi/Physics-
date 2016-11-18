#Autor: Lucas Giraldi Almeida Coimbra
#Idade: 15
#Email para contato: lucasgiraldiac@gmail.com
#Versão 1.0.0

"""Programa criado para facilitar a vida de alunos do ensino médio que já cansaram de fazer tantas fórmulas!"""

command = ""
print("Fala, beleza?")
while command != "FINALIZAR":
    print("Pra que você quer minha ajuda? Só falar que eu faço!")
    print("1 - Energia")
    print("2 - MRU")
    print("3 - MRUV")
    print("4 - Trabalho")
    print("Ou, para sair, digite 'Finalizar'!")
    command = input("Pode falar!\n")
    command.upper()
