import doctest


class Rectangle:

    def __init__(self, length: int | float, width: int | float):
        """
        Класс, описывающий прямоугольник
        :param: length: длина прямоугольника
        :param: width: ширина прямоугольника

        Пример:
        >>> rectangle = Rectangle(2, 2)
        >>> rectangle.get_perimeter()
        8

        >>> rectangle.get_square()
        4

        >>> rectangle = Rectangle(-1, 2)
        """

        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError(f'Wrong data type of input data: length: {type(length)}, width: {type(width)}!')

        if length <= 0 or width <= 0:
            raise ValueError(f'Value <= 0: {"length" if length <= 0 else ""}, {"width" if width <= 0 else ""}')

        self.length = length
        self.width = width

    def get_square(self) -> int | float:
        """
        Расчет площади прямоугольника
        :return: площадь прямоугольника
        """
        return self.length * self.width

    def get_perimeter(self) -> int | float:
        """
        Расчет периметра прямоугольника
        :return: периметр прямоугольника
        """
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    doctest.testmod()
