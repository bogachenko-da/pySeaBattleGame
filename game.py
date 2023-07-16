from board import Board
from ship import Ship
from dot import Dot
from random import randint
from exception import BoardWrongShipException
from player import AI, User


class Game:
    """
    Класс для представления игрового процесса.

    Arg:
        size (int): размер поля
        user (User()): игрок-пользователь
        user_board (Board()): доска игрока-пользователя
        ai (AI()): игрок-компьютер
        comp_board (Board()): доска игрока-компьютера
    """
    def __init__(self, size=6):
        self.size = size
        user_board = self.random_board()
        comp_board = self.random_board()
        comp_board.hide = True
        self.ai = AI(comp_board, user_board)
        self.user = User(user_board, comp_board)

    def try_board(self):
        """
        Метод генерирующий случайное расположение кораблей на доске
        """
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        """
        Метод, который в любом случае сгенерирует случайное расположение
        кораблей на доске, с помощью метода try_board().
        """
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.user.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-" * 20)
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.user.move()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.user.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()
