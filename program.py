#Autor: Lucas Giraldi Almeida Coimbra
#Idade: 15
#Email para contato: lucasgiraldiac@gmail.com
#Versão 1.0.0

"""Programa criado para facilitar a vida de alunos do ensino médio que já cansaram de fazer tantas fórmulas!"""

import math

comando = ""
print("Fala, beleza?")
while comando != "Finalizar":
    print("Pra que você quer minha ajuda? Só falar que eu faço!")
    print("1 - Energia")
    print("2 - MRU")
    print("3 - MRUV")
    print("4 - Trabalho")
    print("Ou, para sair, digite 'Finalizar'!")
    comando = input("Pode falar: ")
    
    if comando = "1":
        print("Qual a fórmula?")
        print("1 - Energia Cinética")
        print("2 - Energia Potencial Gravitacional")
        print("3 - Energia Potencial Elástica")
        energia = input("Pode falar: ")
        
        if energia = "1":
            print("Qual dos dados você precisa saber?")
            print("1 - Energia")
            print("2 - Massa")
            print("3 - Velocidade")
            dado = input("Só digitar: ")
            
            if dado = "1":
                print("Okay! Me fala agora a massa e a velocidade!")
                massa = input("Massa: ")
                velocidade = input("Velocidade: ")
                energia_cinetica = (massa * pow(velocidade, 2)) / 2
                print("A energia cinética do corpo é ", energia_cinetica)
            else:
                if dado = "2":
                    print("Okay! Me fala agora a energia e a velocidade!")
                    energia_cinetica = input("Energia: ")
                    velocidade = input("Velocidade: ")
                    massa = (energia_cinetica * 2) / pow(velocidade, 2)
                    print("A massa do corpo é ", massa)
                else:
                    if dado = "3":
                        print("Okay! Me fala agora a energia e a massa")
                        energia_cinetica = input("Energia: ")
                        massa = input("Massa: ")
                        velocidade = math.sqrt((energia_cinetica * 2) / massa)
                        print("A velocidade do corpo é ", velocidade)
                    else:
                        print("Digite um número válido!")
        else:
            if energia = "2":
                print("Qual dos dados você precisa saber?")
                print("1 - Energia")
                print("2 - Massa")
                print("3 - Aceleração da Gravidade")
                print("4 - Altura")
                dado = input("Só digitar: ")
                
                if dado = "1":
                    print("Okay! Me fala agora a massa, a aceleração da gravidade e a altura!")
                    massa = input("Massa: ")
                    gravidade = input("Aceleração da Gravidade: ")
                    altura = input("Altura: ")
                    energia_potencia_gravitacional = massa * gravidade * altura
                    print("A energia potencial gravitacional do corpo é ", energia_potencial_gravitacional)
                else:
                    if dado = "2":
                        print("Okay! Me fala agora a energia, a aceleração da gravidade e a altura!")
                        energia_potencia_gravitacional = input("Energia: ")
                        gravidade = input("Aceleração da Gravidade: ")
                        altura = input("Altura: ")
                        massa = energia_potencia_gravitacional / (gravidade * altura)
                        print("A massa do corpo é ", massa)
                    else:
                        if dado = "3":
                            print("Okay! Me fala agora a energia, a massa e a altura!")
                            energia_potencia_gravitacional = input("Energia: ")
                            massa = input("Massa: ")
                            altura = input("Altura: ")
                            gravidade = energia_potencia_gravitacional / (massa * altura)
                            print("A aceleração da gravidade local é ", gravidade)
                        else:
                            if dado = "4":
                                print("Okay! Me fala agora a energia, a massa e a aceleração da gravidade!")
                                energia_potencia_gravitacional = input("Energia: ")
                                gravidade = input("Aceleração da Gravidade: ")
                                massa = input("Massa: ")
                                altura = energia_potencia_gravitacional / (gravidade * massa)
                                print("A massa do corpo é ", massa)
                            else:
                                print("Digite um número válido!")
