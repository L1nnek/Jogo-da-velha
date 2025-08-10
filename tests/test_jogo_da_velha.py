import pytest
from jogo_da_velha import tabuleiro, reiniciar_tabuleiro, verificar_vencedor, verificar_empate


def test_verificar_vencedor_linha():
    reiniciar_tabuleiro()
    tabuleiro[0] = ['X', 'X', 'X']
    assert verificar_vencedor('X') is True


def test_verificar_vencedor_coluna():
    reiniciar_tabuleiro()
    for linha in tabuleiro:
        linha[0] = 'O'
    assert verificar_vencedor('O') is True


def test_verificar_vencedor_diagonal_principal():
    reiniciar_tabuleiro()
    tabuleiro[0][0] = tabuleiro[1][1] = tabuleiro[2][2] = 'X'
    assert verificar_vencedor('X') is True


def test_verificar_vencedor_diagonal_secundaria():
    reiniciar_tabuleiro()
    tabuleiro[0][2] = tabuleiro[1][1] = tabuleiro[2][0] = 'O'
    assert verificar_vencedor('O') is True


def test_verificar_empate():
    reiniciar_tabuleiro()
    padrao = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X'],
    ]
    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = padrao[i][j]
    assert verificar_empate() is True
    assert not verificar_vencedor('X')
    assert not verificar_vencedor('O')


def test_verificar_empate_false():
    reiniciar_tabuleiro()
    tabuleiro[0][0] = 'X'
    assert verificar_empate() is False
