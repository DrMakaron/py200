"""
Bad practice



class Duck:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"


    def greet(self, duck2: "Duck"):
        print(f"{self.name}: {self.do_sound()}, hello {duck2.name}")

    # класс описывает утку. greet метод явно лишний: его уместно использовать в классе-коммуникаторе
"""


class Duck:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    @staticmethod
    def do_sound() -> str:
        return "Quack"


class Communicator:

    # TODO Подумать нужен ли конструктор для класса и параметры для передачи в класс
    # def __init__(self):
    #     pass

    # TODO Реализовать класс для взаимодействия двух и БОЛЕЕ уток
    @staticmethod
    def communicate(*ducks: Duck):
        res = []

        for duck in ducks:
            tmp = [duck.name for duck in ducks]
            tmp.remove(duck.name)
            res.append(f"{duck.name} say '{duck.do_sound()}!' to {' and '.join(tmp)}")

        return '; '.join(res)



duck_1 = Duck("Duck_1")
duck_2 = Duck("Duck_2")
duck_3 = Duck("Duck_3")
duck_4 = Duck("Duck_4")
duck_5 = Duck("Duck_5")
duck_6 = Duck("Duck_6")

communicator = Communicator()
# result = communicator.communicate(duck_1, duck_2)
# print(result)  # -> "Duck_1 поприветсвовала Duck_2, Duck_2 поприветствовала Duck_1"
print(communicator.communicate(duck_1, duck_2))
print(communicator.communicate(duck_1, duck_2, duck_3))
print(communicator.communicate(duck_1, duck_2, duck_3, duck_4))
print(communicator.communicate(duck_1, duck_2, duck_3, duck_4, duck_5))
print(communicator.communicate(duck_1, duck_2, duck_3, duck_4, duck_5, duck_6))