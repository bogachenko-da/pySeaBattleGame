from random import randint
from exception import BoardException
from dot import Dot


class Player:
    """
    Базовый класс для представления игрока.

    Arg:
        board (Board()): доска игрока
        enemy (Board()): доска противника
    """

    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        """
        Метод для потомков класса Player.
        Если вызвать метод через класс Player, возникает исключение для указания,
        что метод ask класса Player не реализован.
        """
        raise NotImplementedError()

    def move(self):
        """
        Метод для осуществления хода в игре.
        """
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    """
    Класс для представления игрока-компьютер. Родитель: Player.
    """

    def ask(self):
        """
        Метод, который случайным образом генерирует координаты клетки,
        в которую будет осуществлен выстрел.
        """
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    """
    Класс для представления игрока. Родитель: Player.
    """

    def ask(self):
        """
        Метод, который спрашивает из консоли координаты точки,
        в которую будет осуществлен выстрел.
        """
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print("Введите 2 координаты!")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите числа!")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)
