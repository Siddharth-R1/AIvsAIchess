import chess
import chess.engine

class AIGame:
    def __init__(self, stockfish_path):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

    def make_ai_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=0.1))
        move = result.move
        self.board.push(move)
        return move

    def is_game_over(self):
        return self.board.is_game_over()

    def get_fen(self):
        return self.board.fen()

    def reset_board(self):
        self.board.reset()
