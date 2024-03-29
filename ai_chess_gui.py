import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import chess
from ai_chess_game import AIGame

class ChessGUI:
    def __init__(self, master, stockfish_path):
        self.master = master
        self.game = AIGame(stockfish_path)
        self.board_image = ImageTk.PhotoImage(Image.open('wood_texture.jpg'))
        self.initialize_gui()

    def initialize_gui(self):
        self.master.title("Sid's AIvsAI chess v1.0")
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                x0, y0 = col * 50, row * 50
                x1, y1 = x0 + 50, y0 + 50
                color = "white" if (row + col) % 2 == 0 else "grey"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.update_pieces()

    def update_pieces(self):
        self.canvas.delete("piece")
        for square, piece in self.game.board.piece_map().items():
            row, col = chess.square_rank(square), chess.square_file(square)
            x, y = col * 50 + 25, (7 - row) * 50 + 25
            piece_color = 'white' if piece.color else 'black'
            piece_type = piece.symbol().upper()
            self.canvas.create_text(x, y, text=piece_type, fill=piece_color, font=('Arial', 24, 'bold'), tags='piece')

def main():
    STOCKFISH_PATH = '/opt/homebrew/bin/stockfish' 
    root = tk.Tk()
    gui = ChessGUI(root, STOCKFISH_PATH)
    play_game(gui)
    root.mainloop()

def play_game(gui):
    while not gui.game.is_game_over():
        move = gui.game.make_ai_move()
        gui.update_pieces()
        gui.master.update()
    winner = "White" if gui.game.board.result() == "1-0" else "Black"
    messagebox.showinfo("Game Over", f"{winner} wins!")

if __name__ == "__main__":
    main()
