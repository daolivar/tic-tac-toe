from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()
    game.board = [' '] * 9
    game.current_player = game.player1_symbol

    print("Tic Tac Toe!")
    while True:
        game.display_board()
        break

    option = input("Continue playing? (Y/N) ")
    if option == "Y" or option == "y":
        main()
    else:
        print("Thanks for playing!")
        exit()

if __name__ == "__main__":
    main()