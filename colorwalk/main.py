import tkinter as tk
from tkinter import messagebox
import random
import time

class ColorWalkGUI:
    def __init__(self, master, rows, cols):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.colors = ["red", "yellow", "green", "blue", "purple"]
        self.board = [[random.choice(self.colors) for _ in range(cols)] for _ in range(rows)]
        self.create_widgets()
        self.display_board()
        self.start_time = time.time()

    def create_widgets(self):
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack()

        self.color_buttons = []
        for color in self.colors:
            button = tk.Button(self.buttons_frame, bg=color, width=4, height=2, command=lambda c=color: self.remove_color(c))
            button.pack(side=tk.LEFT)
            self.color_buttons.append(button)

        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        self.cells = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                cell = tk.Label(self.board_frame, bg="white", width=4, height=2, borderwidth=1, relief="solid")
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

    def display_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                color = self.board[i][j]
                self.cells[i][j].config(bg=color)

    def remove_color(self, color):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == color:
                    self.board[i][j] = "white"
        self.display_board()
        if self.check_win():
            self.end_time = time.time()
            self.show_win_message()

    def check_win(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != "white":
                    return False
        return True

    def show_win_message(self):
        total_time = self.end_time - self.start_time
        minutes = int(total_time / 60)
        seconds = int(total_time % 60)
        messagebox.showinfo("Congratulations!", f"You cleared the board in {minutes} minutes and {seconds} seconds.")

# Main program
if __name__ == "__main__":
    rows = 5
    cols = 5
    root = tk.Tk()
    root.title("Color Walk")
    game = ColorWalkGUI(root, rows, cols)
    root.mainloop()
