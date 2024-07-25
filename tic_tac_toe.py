class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.player1_symbol = 'X'
        self.player2_symbol = 'O'
        self.current_player = self.player1_symbol

    def display_board(self):
        print('- - - - - - -')
        for i in range(0, len(self.board), 3):
            print(f'| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |')
            print('- - - - - - -')