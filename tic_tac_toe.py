class TicTacToe:

    def __init__(self):
        """
        Initialize the Tic Tac Toe game.
        Sets up the game board with 9 empty spaces, 
        assigns symbols for player 1 and player 2, 
        and sets the current player to player 1.
        """
        self.board = [' '] * 9
        self.player1_symbol = 'X'
        self.player2_symbol = 'O'
        self.current_player = self.player1_symbol

    def display_instructions(self):
        """
        Display the instructions for playing Tic Tac Toe.
        Prompts the user to press Enter to continue.
        The instructions include how to make a move and the board layout.
        """
        user_input = " "
        while user_input != "":
            print("Welcome to Tic Tac Toe!")
            print("Player 1 is X and Player 2 is O")
            print("To make a move, enter a number between 1 and 9 corresponding to the board position:\n")
            print('1 | 2 | 3')
            print('---------')
            print('4 | 5 | 6')
            print('---------')
            print('7 | 8 | 9\n')
            user_input = input("Press Enter to continue: ")
        for _ in range(5):
            print("\n")

    def display_board(self):
        """
        Display the current state of the game board.
        Shows the board with the current symbols placed.
        """
        print("Tic Tac Toe\n")
        for i in range(0, len(self.board), 3):
            if i == 6:
                print(f' {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} \n')
            else:
                print(f' {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ')
                print(' ––––––––– ')

    def switch_player(self):
        """
        Switch the current player to the other player.
        If the current player is player 1, switch to player 2, and vice versa.
        """
        if self.current_player == self.player1_symbol:
            self.current_player = self.player2_symbol
        else:
            self.current_player = self.player1_symbol

    def get_valid_position(self):
        """
        Prompt the current player to enter a valid position on the board.
        Continue prompting until a valid position is provided.
        
        Returns:
            str: The valid position entered by the player.
        """
        valid = False
        position = None
        while not valid:
            position = input("Enter a position from 1 to 9: ")
            if self.is_valid_position(position):
                index = int(position) - 1
                if self.board[index] == ' ':
                    valid = True
                else:
                    print("Invalid move. The position is already taken. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        return position

    def is_valid_position(self, position):
        """
        Check if the provided position is a valid digit between 1 and 9.

        Args:
            position (str): The position to check.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        return position.isdigit() and 1 <= int(position) <= 9

    def update_board(self, position):
        """
        Update the board with the current player's symbol at the given position.

        Args:
            position (str): The position to update on the board.
        """
        self.board[int(position)-1] = self.current_player

    def check_draw(self):
        """
        Check if the game is a draw.
        A draw occurs if there are no empty spaces left on the board.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        for elem in self.board:
            if elem == ' ':
                return False
        return True

    def check_win(self):
        """
        Check if the current player has won the game.
        The game is won if there is a winning combination in rows, columns, or diagonals.

        Returns:
            bool: True if the current player has won, False otherwise.
        """
        return self.check_rows() or self.check_diagonals() or self.check_columns()

    def check_rows(self):
        """
        Check all three rows for a winning combination.

        Returns:
            bool: True if there is a winning combination in any row, False otherwise.
        """
        return (
            self.current_player == self.board[0] == self.board[1] == self.board[2] or
            self.current_player == self.board[3] == self.board[4] == self.board[5] or
            self.current_player == self.board[6] == self.board[7] == self.board[8]
        )

    def check_diagonals(self):
        """
        Check both diagonals for a winning combination.

        Returns:
            bool: True if there is a winning combination in either diagonal, False otherwise.
        """
        return (
            self.current_player == self.board[0] == self.board[4] == self.board[8] or
            self.current_player == self.board[2] == self.board[4] == self.board[6]
        )

    def check_columns(self):
        """
        Check all three columns for a winning combination.

        Returns:
            bool: True if there is a winning combination in any column, False otherwise.
        """
        return (
            self.current_player == self.board[0] == self.board[3] == self.board[6] or
            self.current_player == self.board[1] == self.board[4] == self.board[7] or
            self.current_player == self.board[2] == self.board[5] == self.board[8]
        )

    def reset_game(self):
        """
        Reset the game board and set the current player to player 1.
        """
        self.board = [' '] * 9
        self.current_player = self.player1_symbol
