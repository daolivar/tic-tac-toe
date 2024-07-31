from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()
    game.board = [' '] * 9
    game.current_player = game.player1_symbol

    print("Tic Tac Toe!")
    while True:
        game.display_board()
        print(f"Current Player {game.current_player}")
        pos = game.get_valid_position()
        game.update_board(pos)
        if game.check_win():
            print(f"Winner, Player {game.current_player}")
            break
        if game.check_draw():
            print(f"Draw, no winner!")
            break
        game.switch_player()

    option = input("Continue playing? (Y/N) ")
    if option == "Y" or option == "y":
        main()
    else:
        print("Thanks for playing!")
        exit()

if __name__ == "__main__":
    main()
