from dot import Dot


class Ship:
    """
    Класс для представления корабля на игровом поле.

    Arg:
        length (int): передается длина корабля
        bow (Dot(x, y)): передается точка, где размещён нос корабля
        orientation (int): передаётся направление корабля (0-вертикальное/1-горизонтальное)
        number_lives (int): передается количество жизней (сколько точек корабля ещё не подбито)
    """
    def __init__(self, bow, length, orientation):
        self.bow = bow
        self.length = length
        self.orientation = orientation
        self.number_lives = length

    @property
    def dots(self):
        """
        Метод для создания списка точек всего корабля,
        исходя из его длины, точки носа корабля и ориентации.
        :return: list
        """
        ship_dots = []
        for i in range(self.length):
            current_x = self.bow.x
            current_y = self.bow.y

            if self.orientation == 0:
                current_x += i

            elif self.orientation == 1:
                current_y += i

            ship_dots.append(Dot(current_x, current_y))

        return ship_dots

    def shooten(self, shot):
        """
        Метод для выстрела, показывает попадание в корабль
        :param shot: Dot(x, y)
        :return: bool
        """
        return shot in self.dots
