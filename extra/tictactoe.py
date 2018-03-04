class Board():
    def __init__(self):
        self.board = [[x for x in range(3*n-2, 3*n+1)] for n in range(1, 4)]
        self.used_blocks = set()

    def __str__(self):
        board_output = ""
        for row in self.board:
            for number in row:
                board_output += str(number) + " "
            board_output += "\n"
        return board_output

    def player_move(self, user_play, steps):
        def _num_to_coord(num):
            """
            1 = (0,0)
            ...
            3 = (0,2)
            ...
            4 = (1,0)
            ...
            9 = (2,0)
            """
            if num % 3 == 0:
                c = 2
                r = num // 3 - 1
            else:
                c = num % 3 - 1
                r = num  // 3
            return (r,c)
        num = int(user_play) # change the user's input to an int
        if num in self.used_blocks: 
            print("You already used this block")
            return True
        
        self.used_blocks.add(num) # keep track of the newly used block
        # determine whether we need x or o
        if steps % 2 == 0: # need x
            symbol = "x"
        else: # need o
            symbol = "o"
        (r,c) = _num_to_coord(num)
        self.board[r][c] = symbol
        return False

    def game_state(self):
        """
        Returns either "x", "o", "tie"
        or None according to who wins
        """
        # check for a win by columns, rows, and diagonals
        # check the columns
        columns = [[self.board[c][r] for c in range(3)] for r in range(3)]
        for column in columns:
            if column.count(column[0]) == len(column):
                return column[0] # return the winning symbol
        # check the rows
        rows = [[self.board[r][c] for c in range(3)] for r in range(3)]
        for row in rows:
            if row.count(row[0]) == len(row):
                return row[0] # return the winning symbol 
        # check the diagonals
        main = [self.board[n][n] for n in range(3)] # main diagonal
        anti = [self.board[n][2-n] for n in range(3)] # antidiagonal
        if main.count(main[0]) == len(main) or anti.count(anti[0]) == len(anti):
                # return the center element - common to both diagonals
                return self.board[1][1]
        # check for a tie
        if len(self.used_blocks) == 9:
            return "tie"
        # neither a win nor a tie ==> ongoing
        return None

board = Board()
steps = 0
while board.game_state() == None:
    print()
    print(board)
    user_play = input("Enter the number of the square you'd like to choose: ")
    user_mistake = board.player_move(user_play, steps)
    if not user_mistake:
        steps += 1
print(board)
game_state = board.game_state()
if game_state != "tie":
    print(game_state + " won!")
else:
    print("The game is a tie")







