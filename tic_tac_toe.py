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

    def display_board(self):
        # Display the current state of the board
        print('- - - - - - -')
        for i in range(0, len(self.board), 3):
            print(f'| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |')
            print('- - - - - - -')

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
        pos = None
        while not valid:
            # Get user input for the position
            pos = input("Enter a position from 1 to 9: ")
            # Check if the input is a valid position
            if self.is_valid_position(pos):
                index = int(pos) - 1  # Convert to 0-based index
                # Check if the board position is empty
                if self.board[index] == ' ':
                    valid = True
                else:
                    print("Invalid move. The position is already taken. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        return pos

    def is_valid_position(self, position):
        # Check if the input is a digit and is between 1 and 9
        return position.isdigit() and 1 <= int(position) <= 9

    def update_board(self, position):
        # Update the board with the current player's symbol at the given position.
        self.board[int(position)-1] = self.current_player
