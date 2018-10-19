def predict_human(board, computer, human):
    # Function to predict the move of the human, returns the next potential board
    board = board[:]
    # Making a copy of the board list

    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    # Check to see if the human can make any winning moves
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            return move
        board[move] = EMPTY

    return None

def computer_move(board, computer, human):
    board = [:]
    # Making a copy of the board list

    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    # If the computer can take a winning move, do that
    for moves in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            return move
        board[move] = EMPTY

    # If human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            return move
        board[move] = EMPTY

    next_computer_move = predict_human(board, computer, human)
    """
    At this point it would be best to predict the human's next move
    and base the next move off of that prospective board.
    """ 
    if next_computer_move is not None:
        return next_computer_move
    else:
        for move in BEST_MOVES:
            if move in legal_moves(board):
                return move
