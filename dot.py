class Dot:
    """
    Класс для представления точек на игровом поле.

    Arg:
        x(int): передается координата x
        y(int): передается координата y
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        Метод для сравнения двух объектов
        :param other: передается обьект для сравнения
        :return: bool
        """
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """
        Метод для вывода точек в консоль
        :return: Dot(x, y)
        """
        return f"Dot({self.x}, {self.y})"
