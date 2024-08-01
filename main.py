from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()
    reset = True

    while True:
        if reset:
            game.reset_game()  # Reset the game state
            game.display_instructions()
            reset = False

        game.display_board()
        print(f"Current Player {game.current_player}")
        pos = game.get_valid_position()
        game.update_board(pos)

        if game.check_win():
            game.display_board()
            print(f"Winner, Player {game.current_player}")
            reset = True
        elif game.check_draw():
            game.display_board()
            print("Draw, no winner!")
            reset = True
        else:
            game.switch_player()

        if reset:
            option = input("Continue playing? (Y/N) ")
            if option.lower() != 'y':
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    main()
