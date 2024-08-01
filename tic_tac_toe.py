class TicTacToe:
    def __init__(self):
        # Initialize the game board with 9 empty spaces
        self.board = [' '] * 9
        # Set player 1's symbol to 'X'
        self.player1_symbol = 'X'
        # Set player 2's symbol to 'O'
        self.player2_symbol = 'O'
        # Set the current player to player 1 initially
        self.current_player = self.player1_symbol

    def display_instructions(self):
        # Initialize user_input with a non-empty string to enter the while loop
        user_input = " "

        # Loop until the user presses Enter without typing anything
        while user_input != "":
            # Display the instructions for the game
            print("Welcome to Tic Tac Toe!")
            print("Player 1 is X and Player 2 is O")
            print("To make a move, enter a number between 1 and 9 corresponding to the board position:\n")
            
            # Display the board positions corresponding to the numbers 1 to 9
            print('1 | 2 | 3')
            print('---------')
            print('4 | 5 | 6')
            print('---------')
            print('7 | 8 | 9\n')
            
            # Prompt the user to press Enter to continue
            user_input = input("Press Enter to continue: ")

        # Print 5 new lines to clear the screen after the instructions
        for _ in range(5):
            print("\n")

    def display_board(self):
        # Display the current state of the board
        print("Tic Tac Toe\n")
        for i in range(0, len(self.board), 3):
            if i == 6:
                print(f' {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} \n')
            else:
                print(f' {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ')
                print(' ––––––––– ')

    def switch_player(self):
        # Switch to the other player
        if self.current_player == self.player1_symbol:
            self.current_player = self.player2_symbol
        else:
            self.current_player = self.player1_symbol

    def get_valid_position(self):
        # Prompt the current player to enter a valid position on the board
        # Continue prompting until a valid position is provided
        valid = False
        position = None
        while not valid:
            # Get user input for the position
            position = input("Enter a position from 1 to 9: ")
            # Check if the input is a valid position
            if self.is_valid_position(position):
                index = int(position) - 1  # Convert to 0-based index
                # Check if the board position is empty
                if self.board[index] == ' ':
                    valid = True
                else:
                    print("Invalid move. The position is already taken. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        return position

    def is_valid_position(self, position):
        # Check if the input is a digit and is between 1 and 9
        return position.isdigit() and 1 <= int(position) <= 9

    def update_board(self, position):
        # Update the board with the current player's symbol at the given position.
        self.board[int(position)-1] = self.current_player

    def check_draw(self):
        for elem in self.board:
            # If there is at least one empty space, the game is not a draw
            if elem == ' ':
                return False
        return True

    def check_win(self):
        # Check rows, diagonals, and columns for a winning combination
        return self.check_rows() or self.check_diagonals() or self.check_columns()

    def check_rows(self):
        # Check all three rows
        return (
            self.current_player == self.board[0] == self.board[1] == self.board[2] or
            self.current_player == self.board[3] == self.board[4] == self.board[5] or
            self.current_player == self.board[6] == self.board[7] == self.board[8]
        )

    def check_diagonals(self):
        # Check both diagonals
        return (
            self.current_player == self.board[0] == self.board[4] == self.board[8] or
            self.current_player == self.board[2] == self.board[4] == self.board[6]
        )

    def check_columns(self):
        # Check all three columns
        return (
            self.current_player == self.board[0] == self.board[3] == self.board[6] or
            self.current_player == self.board[1] == self.board[4] == self.board[7] or
            self.current_player == self.board[2] == self.board[5] == self.board[8]
        )

    def reset_game(self):
        # Reset the game board and set the current player to player 1
        self.board = [' '] * 9
        self.current_player = self.player1_symbol
