from tkinter import *
import copy
import random


class Grid:

    def __init__(self):
        self.n = 9
        self.window_width = 630
        self.window_height = 630
        self.buttons = [
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '']
        ]
        self.base_grid = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
            ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
            ['2', '3', '4', '5', '6', '7', '8', '9', '1'],
            ['5', '6', '7', '8', '9', '1', '2', '3', '4'],
            ['8', '9', '1', '2', '3', '4', '5', '6', '7'],
            ['3', '4', '5', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
            ['9', '1', '2', '3', '4', '5', '6', '7', '8']
        ]
        self.game_grid = [
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '']
        ]
        self.temp_grid = None
        self.root = Tk()
        self.root.title('Sudoku by Hollow')
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        self.menu = Menu(self.root, tearoff=False)
        self.menu.add_command(label='Новая Игра', command=self.__new_game)
        self.menu.add_command(label='Правила', command=self.__new_game)
        self.root.configure(bg="#DCDCDC", menu=self.menu)
        self.root.resizable(width=False, height=False)
        self.frame = Frame(self.root, bg="#F5FFFA", bd=1, width=self.window_width, height=self.window_height)

    def start(self):
        self.root.mainloop()
        return 0

    def __new_game(self):
        self.frame.pack(expand=True)
        self.__transposing()
        self.__swap_rows(iterations=random.randint(5, 100))
        for row in range(self.n):
            for column in range(self.n):
                self.buttons[row][column] = Button(self.frame, text=f"{self.game_grid[row][column]}", bd=3,
                                                   bg="#F5FFFA", fg="#000000", activebackground="#008000",
                                                   font='TimesNewRoman 16', width=4, height=2)
                self.buttons[row][column].grid(row=row + 1, column=column + 1)

    def __transposing(self):
        i = 0
        j = 0
        for row in range(self.n):
            for r in range(self.n):
                self.game_grid[r][i] = self.base_grid[row][r]
                j += 1
            i += 1
        self.temp_grid = copy.deepcopy(self.game_grid)

    def __swap_rows(self, iterations):
        for i in range(iterations):
            row1 = random.randint(0, 8)
            row2 = random.randint(0, 8)
            if (row1 == row2) and (row2 < 8):
                row2 += 1
            else:
                row1 -= 1
            for j in range(self.n):
                self.game_grid[row1][j] = self.temp_grid[row2][j]
                self.game_grid[row2][j] = self.temp_grid[row1][j]
            print(row1+1, row2+1)
        self.temp_grid = copy.deepcopy(self.game_grid)

    def __swap_colums(self):
        pass


if __name__ == '__main__':
    start = Grid().start()
