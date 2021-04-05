from random import choice #Importando a função choice da biblioteca random

comp_vitorias = 0 #Variável para contar vitorias
jogador_vitorias = 0 #Variável para contar vitorias do jogador

def Opcao_Jogador(): #Definindo função opção do jogador
    esc_jogador = "" #Limpando variável da escolha do jogador
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ") #Input de entrada de dados
    if esc_jogador in ["Pedra", "PEDRA", "pedra"]: esc_jogador = "pedra" #Se jogador digitar PEDRA, guarde valor pedra na variável esc_jogador
    elif esc_jogador in ["Papel", "PAPEL", "papel"]: esc_jogador = "papel" #Se jogador digitar PAPEL, guarde valor PAPEL na variável esc_jogador
    elif esc_jogador in ["Tesoura", "TESOURA", "tesoura"]: esc_jogador = "tesoura" #Se jogador digitar TESOURA, guarde valor TESOURA na variável esc_jogador
    else: #Se não for nenhuma das opções acima
        print("Opção Inválida. Tente Novamente")
        Opcao_Jogador() #Chama função opção do jogador novamente
    return esc_jogador

def Opcao_Computador():
    esc_computador = choice(["pedra", "papel", "tesoura"]) #Escolha aleatória do computador
    return esc_computador


while True:

    print("---------------")

    esc_computador = Opcao_Computador() #Chama função opção do computador
    esc_jogador = Opcao_Jogador() #Chama função opção do jogador

    print("---------------")

    #Analisando condições de entradas do jogo
    if (esc_jogador == "papel") and (esc_computador == "pedra"): #Se o jogador escolheu papel e o computador pedra
        print(f"O Jogador escolheu {esc_jogador} e o Computador escolheu {esc_computador}, sendo o Resultado: Jogador Ganhou")
        jogador_vitorias += 1 #Soma uma vitória para o jogador

    elif (esc_jogador == "pedra") and (esc_computador == "tesoura"): #Se o jogador escolheu pedra e o computador tesoura
        print(f"O Jogador escolheu {esc_jogador} e o Computador escolheu {esc_computador}, sendo o Resultado: Jogador Ganhou")
        jogador_vitorias += 1 #Soma uma vitória para o jogador

    elif (esc_jogador == "tesoura") and (esc_computador == "papel"): #Se o jogador escolheu tesoura e o computador papel
        print(f"O Jogador escolheu {esc_jogador} e o Computador escolheu {esc_computador}, sendo o Resultado: Jogador Ganhou")
        jogador_vitorias += 1 #Soma uma vitória para o jogador

    elif (esc_jogador == esc_computador): #Se der empate - Não conta ponto
        print(f"O Jogador escolheu {esc_jogador} e o Adversário escolheu {esc_computador}, sendo o Resultado: Empate")

    else:  #Se o jogador escolheu qualquer outra situação que não seja de vitória
        print(f"O Jogador escolheu {esc_jogador} e o Adversário escolheu {esc_computador}, sendo o Resultado: Computador Ganhou")
        comp_vitorias += 1 #Soma uma vitória para o computador
    
    print("-----------------")

    print(f"Vitorias do Jogador: {jogador_vitorias}") #Imprime contador de vitórias do jogador
    print(f"Vitorias do Computador: {comp_vitorias}") #Imprime contator de vitórias do Computador

    print("-----------------")

    #Condição SE o jogador quer continuar o game
    esc_jogador = input("Você quer jogar novamente (s/n): ")
    if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]: #SE SIM
        pass #Repete o laço
    elif esc_jogador in ["NAO", "nao", "Nao", "N", "n"]: #SE NÃO
        break #Encerra o game
    else:
        break #Qualquer outra coisa, encerra o game