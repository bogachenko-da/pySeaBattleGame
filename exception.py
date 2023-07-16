class BoardException(Exception):
    """
    Базовый класс для представления исключений. Родитель: Exception.
    """
    pass


class BoardOutException(BoardException):
    """
    Класс для представления исключения, если пользователь попытается выстрелить за игровое поле.
    """
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"


class BoardUsedException(BoardException):
    """
    Класс для представления исключения, если пользователь уже стрелял в эту клетку игрового поля.
    """
    def __str__(self):
        return "Вы уже стреляли в эту клетку"


class BoardWrongShipException(BoardException):
    """
    Класс для представления исключения, при неправильном размещении кораблей на игровом поле.
    """
    pass
