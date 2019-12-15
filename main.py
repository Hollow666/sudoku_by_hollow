from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import copy
import random


class Game:

    def __init__(self):
        self.n = 9
        self.window_width = 630
        self.window_height = 630
        self.button_bg_color = '#F5FFFA'
        self.button_activebg_color = '#008000'
        self.key_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
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
        self.root.iconbitmap(r'C:\projects\Python\Sudoku by Hollow\ico.ico')
        self.root.title('Sudoku by Hollow')
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        self.menu = Menu(self.root, tearoff=False)
        self.menu.add_command(label='Новая Игра', command=self.__new_game)
        self.menu.add_command(label='Проверить', command=self.__inspect)
        self.root.configure(bg="#DCDCDC", menu=self.menu)
        self.root.resizable(width=False, height=False)
        self.frame = Frame(self.root, bg="#F5FFFA", bd=1, width=self.window_width, height=self.window_height)

    def start(self):
        self.root.mainloop()
        return 0

    def __new_game(self):
        self.frame.pack(expand=True)
        self.__transposing()
        self.__swap_rows_in_section()
        self.__swap_columns_in_section()
        self.__random_delete()
        for row in range(self.n):
            for column in range(self.n):
                self.buttons[row][column] = Button(self.frame, text=f"{self.game_grid[row][column]}", bd=3,
                                                   bg="#F5FFFA", fg="#000000", activebackground="#008000",
                                                   font='TimesNewRoman 16', width=4, height=2,
                                                   command=lambda row=row, column=column: self.__click(
                                                                                       row=row, column=column))
                button = self.buttons[row][column]
                if button['text'] == '':
                    button['bg'] = "#E6E6FA"
                self.buttons[row][column].grid(row=row + 1, column=column + 1)
        #for row in range(self.n):
            #print(self.temp_grid[row])

    def __transposing(self):
        i = 0
        j = 0
        for row in range(self.n):
            for r in range(self.n):
                self.game_grid[r][i] = self.base_grid[row][r]
                j += 1
            i += 1
        self.temp_grid = copy.deepcopy(self.game_grid)

    def __swap_rows_in_section(self):
        for section in range(1, 4, 1):
            for iteration in range(3):
                if section == 1:
                    row1 = random.randint(0, 2)
                    row2 = random.randint(0, 2)
                    #if (row1 == row2):
                        #if row2 > 5:
                            #row2 -=2
                        #else:
                            #row2 +=2
                    for j in range(self.n):
                        self.game_grid[row1][j] = self.temp_grid[row2][j]
                        self.game_grid[row2][j] = self.temp_grid[row1][j]
                    self.temp_grid = copy.deepcopy(self.game_grid)
                if section == 2:
                    row1 = random.randint(3, 5)
                    row2 = random.randint(3, 5)
                    #if (row1 == row2):
                        #if row2 > 5:
                            #row2 -=2
                        #else:
                            #row2 +=2
                    for j in range(self.n):
                        self.game_grid[row1][j] = self.temp_grid[row2][j]
                        self.game_grid[row2][j] = self.temp_grid[row1][j]
                    self.temp_grid = copy.deepcopy(self.game_grid)
                if section == 3:
                    row1 = random.randint(6, 8)
                    row2 = random.randint(6, 8)
                    #if (row1 == row2):
                        #if row2 > 5:
                            #row2 -=2
                        #else:
                            #row2 +=2
                    for j in range(self.n):
                        self.game_grid[row1][j] = self.temp_grid[row2][j]
                        self.game_grid[row2][j] = self.temp_grid[row1][j]
                    self.temp_grid = copy.deepcopy(self.game_grid)

    def __swap_columns_in_section(self):
        for section in range(1, 4, 1):
            for iteration in range(3):
                if section == 1:
                    column1 = random.randint(0, 2)
                    column2 = random.randint(0, 2)
                    #if (column1 == column2):
                        #if column2 > 5:
                            #column2 -= 2
                        #else:
                            #column2 += 2
                    for j in range(self.n):
                        self.game_grid[j][column1] = self.temp_grid[j][column2]
                        self.game_grid[j][column2] = self.temp_grid[j][column1]
                    self.temp_grid = copy.deepcopy(self.game_grid)
                if section == 2:
                    column1 = random.randint(3, 5)
                    column2 = random.randint(3, 5)
                    #if (column1 == column2):
                        #if column2 > 5:
                            #column2 -= 2
                        #else:
                            #column2 += 2
                    for j in range(self.n):
                        self.game_grid[j][column1] = self.temp_grid[j][column2]
                        self.game_grid[j][column2] = self.temp_grid[j][column1]
                    self.temp_grid = copy.deepcopy(self.game_grid)
                if section == 3:
                    column1 = random.randint(6, 8)
                    column2 = random.randint(6, 8)
                    #if (column1 == column2):
                        #if column2 > 5:
                            #column2 -= 2
                        #else:
                            #column2 += 2
                    for j in range(self.n):
                        self.game_grid[j][column1] = self.temp_grid[j][column2]
                        self.game_grid[j][column2] = self.temp_grid[j][column1]
                    self.temp_grid = copy.deepcopy(self.game_grid)

    def __click(self, row, column):
        button = self.buttons[row][column]
        button['bg'] = "#E6E6FA"
        answer = simpledialog.askstring("Ввод значения", "Введите цифру: ", parent=self.root)
        if answer is not None:
            for key in self.key_list:
                if answer == key:
                    button['text'] = answer
                    answer = ''
                    break

    def __random_delete(self):
        for iteration in range(1, 41, 1):
            row = random.randint(0, 8)
            column = random.randint(0, 8)
            self.game_grid[row][column] = ''

    def __inspect(self):
        count = 0
        for row in range(self.n):
            for column in range(self.n):
                button = self.buttons[row][column]
                if button['text'] != self.temp_grid[row][column]:
                    button['bg'] = "#FF4500"
        for row in range(self.n):
            for column in range(self.n):
                button = self.buttons[row][column]
                if button['bg'] == "#FF4500":
                    count += 1
        if count != 0:
            messagebox.showinfo("Ошибка", "Тщательно проверьте введенные значения!")
        else:
            messagebox.showinfo("Игра завершена", "Поздравляем!!! Вы заполнили все пустые клетки правильно.")


if __name__ == '__main__':
    start = Game().start()
