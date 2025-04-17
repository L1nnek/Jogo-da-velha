import os
import random

# Cria o tabuleiro 3x3 vazio e define coordenadas válidas
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
coordenadas_validas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
P1 = "X"  # Jogador 1
P2 = "O"  # Jogador 2 ou computador


# Limpa a tela do terminal (funciona fora da IDE).
# Em IDEs como PyCharm, pode não funcionar.
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# Mostra o tabuleiro formatado no terminal
def mostrar_tabuleiro():
    print("\n" + "-" * 27)
    print("       JOGO DA VELHA")
    print("         por Línnek")
    print("-" * 27)
    print("\n")
    print("     A   B   C")
    for i, linha in enumerate(tabuleiro):
        linha_formatada = " | ".join(linha)
        print(f"  {i + 1}  {linha_formatada}")
        if i < 2:
            print("    ---+---+---")
    print("\n")


# Reseta o tabuleiro, preenchendo tudo com espaços
def reiniciar_tabuleiro():
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            tabuleiro[linha][coluna] = " "


# Verifica se uma coordenada está livre
def verificar_vaga(coordenada):
    if "A" in coordenada:
        if "1" in coordenada:
            return tabuleiro[0][0] == " "
        elif "2" in coordenada:
            return tabuleiro[1][0] == " "
        elif "3" in coordenada:
            return tabuleiro[2][0] == " "
    elif "B" in coordenada:
        if "1" in coordenada:
            return tabuleiro[0][1] == " "
        elif "2" in coordenada:
            return tabuleiro[1][1] == " "
        else:
            return tabuleiro[2][1] == " "
    else:
        if "1" in coordenada:
            return tabuleiro[0][2] == " "
        elif "2" in coordenada:
            return tabuleiro[1][2] == " "
        else:
            return tabuleiro[2][2] == " "


# Marca o símbolo (X ou O) no tabuleiro conforme a coordenada recebida
def registrar_jogada(coordenada, simbolo):
    if "A" in coordenada:
        if "1" in coordenada:
            tabuleiro[0][0] = simbolo
        elif "2" in coordenada:
            tabuleiro[1][0] = simbolo
        else:
            tabuleiro[2][0] = simbolo
    elif "B" in coordenada:
        if "1" in coordenada:
            tabuleiro[0][1] = simbolo
        elif "2" in coordenada:
            tabuleiro[1][1] = simbolo
        else:
            tabuleiro[2][1] = simbolo
    else:
        if "1" in coordenada:
            tabuleiro[0][2] = simbolo
        elif "2" in coordenada:
            tabuleiro[1][2] = simbolo
        else:
            tabuleiro[2][2] = simbolo
    return


# Verifica se o jogador atual venceu (linhas, colunas ou diagonais)
def verificar_vencedor(simbolo):
    if (
        tabuleiro[0][0] == simbolo
        and tabuleiro[0][1] == simbolo
        and tabuleiro[0][2] == simbolo
        or tabuleiro[1][0] == simbolo
        and tabuleiro[1][1] == simbolo
        and tabuleiro[1][2] == simbolo
        or tabuleiro[2][0] == simbolo
        and tabuleiro[2][1] == simbolo
        and tabuleiro[2][2] == simbolo
        or tabuleiro[0][0] == simbolo
        and tabuleiro[1][0] == simbolo
        and tabuleiro[2][0] == simbolo
        or tabuleiro[0][1] == simbolo
        and tabuleiro[1][1] == simbolo
        and tabuleiro[2][1] == simbolo
        or tabuleiro[0][2] == simbolo
        and tabuleiro[1][2] == simbolo
        and tabuleiro[2][2] == simbolo
        or tabuleiro[0][0] == simbolo
        and tabuleiro[1][1] == simbolo
        and tabuleiro[2][2] == simbolo
        or tabuleiro[0][2] == simbolo
        and tabuleiro[1][1] == simbolo
        and tabuleiro[2][0] == simbolo
    ):
        return True
    return False


# Verifica se todas as casas foram preenchidas (empate)
def verificar_empate():
    preenchidos = 0
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] in ["X", "O"]:
                preenchidos += 1
    return preenchidos == 9


# Pede a jogada ao jogador e valida a entrada
def obter_jogada(simbolo):
    while True:
        resposta = input(
            f"🎮 Jogador {simbolo}, digite uma coordenada (ex: B2): "
        ).upper()
        limpar_tela()
        mostrar_tabuleiro()
        if resposta in coordenadas_validas:
            if verificar_vaga(resposta):
                return resposta
            else:
                print("Já ocupado!\n")
        else:
            print("⚠️ Entrada inválida! Digite uma coordenada como A1, B2")


# Define jogada do computador de forma aleatória entre casas disponíveis
def computador():
    while True:
        escolha = random.choice(coordenadas_validas)
        if verificar_vaga(escolha):
            registrar_jogada(escolha, P2)
            return


# Jogo entre dois jogadores humanos
def jogar_partida():
    vez = 0
    while True:
        simbolo_atual = P1 if vez == 0 else P2
        vez = 1 - vez  # Alterna entre 0 e 1
        jogada_escolhida = obter_jogada(simbolo_atual)
        registrar_jogada(jogada_escolhida, simbolo_atual)
        limpar_tela()
        mostrar_tabuleiro()
        if verificar_vencedor(simbolo_atual):
            print(f"🎉 Jogador {simbolo_atual} venceu o jogo!\n")
            reiniciar_tabuleiro()
            break
        if verificar_empate():
            print("🤝 Deu velha! O tabuleiro está cheio.\n")
            reiniciar_tabuleiro()
            break


# Jogo entre jogador humano e computador
def jogar_partida_vs_computador():
    vez = 0
    while True:
        simbolo_atual = P1 if vez == 0 else P2
        if vez == 0:
            jogada_escolhida = obter_jogada(simbolo_atual)
            if verificar_vaga(jogada_escolhida):
                registrar_jogada(jogada_escolhida, simbolo_atual)
        else:
            computador()
        limpar_tela()
        mostrar_tabuleiro()
        vez = 1 - vez  # Alterna entre jogador e computador
        if verificar_vencedor(simbolo_atual):
            print(f"🎉 Jogador {simbolo_atual} venceu o jogo!\n")
            reiniciar_tabuleiro()
            break
        if verificar_empate():
            print("🤝 Deu velha! O tabuleiro está cheio.\n")
            reiniciar_tabuleiro()
            break


# Menu principal com opções de jogo
def menu_principal():
    mostrar_tabuleiro()
    while True:
        print("🎮 MENU PRINCIPAL")
        print("1 - Jogar contra outro jogador")
        print("2 - Modo contra IA (Fácil)")
        print("3 - Sair\n")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            limpar_tela()
            mostrar_tabuleiro()
            jogar_partida()
        elif escolha == "2":
            limpar_tela()
            mostrar_tabuleiro()
            jogar_partida_vs_computador()
        elif escolha == "3":
            limpar_tela()
            mostrar_tabuleiro()
            print("👋 Valeu por jogar! Até a próxima.\n")
            break
        else:
            limpar_tela()
            mostrar_tabuleiro()
            print("❌ Opção inválida. Tente novamente.\n")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()
