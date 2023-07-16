from dot import Dot
from exception import BoardWrongShipException, BoardOutException, BoardUsedException


class Board:
    """
    Класс для представления игрового поля.

    Arg:
        hide (bool): скрытие поля
        size (int): размер поля
        count_destroyed (int): количество пораженных кораблей
        field (list): сетка игрового поля
        busy (list): список для хранения занятых кораблем точек или точек куда уже стреляли
        ships (list): список точек кораблей на доске
    """
    def __init__(self, hide=False, size=6):
        self.hide = hide
        self.size = size

        self.count_destroyed = 0

        self.field = [["O"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
        """
        Метод для вывода игрового поля, если параметр hide = True, то корабли будут скрыты.
        :return: str
        """
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hide:
            res = res.replace("■", "O")
        return res

    def dot_out(self, dot):
        """
        Метод, который определяет находится ли точка за пределами доски.
        :param dot: Dot(x, y)
        :return: bool
        """
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def contour(self, ship, verb=False):
        """
        Метод, который определяет контур корабля
        :param ship: Dot(x, y)
        :param verb: bool
        """
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                current = Dot(d.x + dx, d.y + dy)
                if not (self.dot_out(current)) and current not in self.busy:
                    if verb:
                        self.field[current.x][current.y] = "."
                    self.busy.append(current)

    def add_ship(self, ship):
        """
        Метод для добавления корабля в список собственных кораблей и в список занятых точек,
        и обведения этого корабля по контуру
        :param ship: Dot(x, y)
        """
        for d in ship.dots:
            if self.dot_out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        """
        Метод для осуществления выстрела, при этом проверяется
        выходит ли точка за границы поля, занята ли точка
        :param d: Dot(x, y)
        :return: bool
        """
        if self.dot_out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.shooten(d):
                ship.number_lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.number_lives == 0:
                    self.count_destroyed += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True
        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        """
        Метод для обнуления списка busy
        """
        self.busy = []
