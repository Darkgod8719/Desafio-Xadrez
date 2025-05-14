import chess

def print_board(board):
    print(board.unicode())  # Mostra o tabuleiro no terminal com peças em unicode

def main():
    board = chess.Board()

    print("Bem-vindo ao jogo de Xadrez!")
    print("Digite movimentos no formato UCI (ex: e2e4, g1f3)")
    print_board(board)

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            print("\n🔵 Vez das BRANCAS")
        else:
            print("\n⚫ Vez das PRETAS")

        move_input = input("Sua jogada: ")

        try:
            move = chess.Move.from_uci(move_input)
            if move in board.legal_moves:
                board.push(move)
                print_board(board)
            else:
                print("Movimento inválido. Tente novamente.")
        except Exception as e:
            print("Erro no movimento:", e)

    print("\n🏁 Fim de jogo!")
    print("Resultado:", board.result())

    if board.is_checkmate():
        print("Xeque-mate!")
    elif board.is_stalemate():
        print("Empate por afogamento.")
    elif board.is_insufficient_material():
        print("Empate por material insuficiente.")
    elif board.is_seventyfive_moves():
        print("Empate por regra dos 75 lances.")
    elif board.is_fivefold_repetition():
        print("Empate por repetição de posição.")

if __name__ == "__main__":
    main()
