"""
Moves Played by the computer after playing. Points are based on the position of the pieces on the board.
For Example if the Queen is in the center of the board it will have a higher score than if it is 
on the edge of the board due to the number of squares it can attack from the center compared to the edge. 
Similarly this is given for other pieces as well. The score is calculated for both the white and black pieces.  
"""

import random

piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

knight_scores = [[0.01, 0.11, 0.19, 0.21, 0.21, 0.19, 0.11, 0.01],
                 [0.09, 0.29, 0.51, 0.51, 0.49, 0.49, 0.29, 0.09],
                 [0.21, 0.51, 0.62, 0.65, 0.65, 0.62, 0.51, 0.21],
                 [0.21, 0.55, 0.65, 0.75, 0.75, 0.65, 0.55, 0.21],
                 [0.21, 0.51, 0.65, 0.75, 0.75, 0.65, 0.51, 0.21],
                 [0.21, 0.55, 0.62, 0.65, 0.65, 0.62, 0.55, 0.21],
                 [0.1, 0.31, 0.51, 0.55, 0.55, 0.51, 0.31, 0.1],
                 [0.0, 0.1, 0.21, 0.21, 0.21, 0.21, 0.1, 0.0]]

bishop_scores = [[0.0, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.0],
                 [0.21, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.21],
                 [0.21, 0.41, 0.51, 0.62, 0.62, 0.51, 0.41, 0.21],
                 [0.21, 0.51, 0.51, 0.62, 0.62, 0.51, 0.51, 0.21],
                 [0.21, 0.41, 0.62, 0.62, 0.62, 0.62, 0.41, 0.21],
                 [0.21, 0.62, 0.62, 0.62, 0.62, 0.62, 0.62, 0.21],
                 [0.21, 0.51, 0.41, 0.41, 0.41, 0.41, 0.51, 0.21],
                 [0.0, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.0]]

rook_scores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.51, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.51, 0.51, 0.25, 0.25, 0.25]]

queen_scores = [[0.0, 0.21, 0.21, 0.31, 0.31, 0.21, 0.21, 0.0],
                [0.21, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.21],
                [0.21, 0.41, 0.51, 0.51, 0.51, 0.51, 0.41, 0.21],
                [0.31, 0.41, 0.51, 0.51, 0.51, 0.51, 0.41, 0.3],
                [0.41, 0.41, 0.51, 0.51, 0.51, 0.51, 0.41, 0.3],
                [0.21, 0.51, 0.51, 0.51, 0.51, 0.51, 0.41, 0.21],
                [0.21, 0.41, 0.51, 0.41, 0.41, 0.41, 0.41, 0.21],
                [0.0, 0.21, 0.21, 0.31, 0.31, 0.21, 0.21, 0.0]]

pawn_scores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.7],
               [0.31, 0.31, 0.41, 0.51, 0.51, 0.41, 0.31, 0.3],
               [0.25, 0.25, 0.31, 0.45, 0.45, 0.31, 0.25, 0.25],
               [0.21, 0.21, 0.21, 0.41, 0.41, 0.21, 0.21, 0.21],
               [0.25, 0.15, 0.1, 0.21, 0.21, 0.1, 0.15, 0.25],
               [0.25, 0.31, 0.31, 0.0, 0.0, 0.31, 0.31, 0.25],
               [0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21]]

piece_position_scores = {"wN": knight_scores,
                         "bN": knight_scores[::-1],
                         "wB": bishop_scores,
                         "bB": bishop_scores[::-1],
                         "wQ": queen_scores,
                         "bQ": queen_scores[::-1],
                         "wR": rook_scores,
                         "bR": rook_scores[::-1],
                         "wp": pawn_scores,
                         "bp": pawn_scores[::-1]}

MATE = 1000 
STALEMATE = 0
DEPTH = 3


def findMoveNegaMaxAlphaBeta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    global next_move
    if depth == 0:
        return turn_multiplier * scoreBoard(game_state)
    max_score = -MATE
    for move in valid_moves:
        game_state.makeMove(move)
        next_moves = game_state.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        game_state.undoMove()
        if max_score > alpha:
            alpha = max_score
        if alpha >= beta:
            break
    return max_score


def scoreBoard(game_state):
    """
    Score the board. White pieces have positive score as good, a negative score is good for black.
    """
    if game_state.checkmate:
        if game_state.white_to_move:
            return -MATE  # black wins
        else:
            return MATE  # white wins
    elif game_state.stalemate:
        return STALEMATE
    score = 0
    for row in range(len(game_state.board)):
        for col in range(len(game_state.board[row])):
            piece = game_state.board[row][col]
            if piece != "--":
                piece_position_score = 0
                if piece[1] != "K":
                    piece_position_score = piece_position_scores[piece][row][col]
                if piece[0] == "w":
                    score += piece_score[piece[1]] + piece_position_score
                if piece[0] == "b":
                    score -= piece_score[piece[1]] + piece_position_score

    return score


def playRandomMove(valid_moves):
    """
    Returns a random valid move after picking it.
    """
    return random.choice(valid_moves)

def playBestMove(game_state, valid_moves, return_queue):
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    findMoveNegaMaxAlphaBeta(game_state, valid_moves, DEPTH, -MATE, MATE,
                             1 if game_state.white_to_move else -1)
    return_queue.put(next_move)
