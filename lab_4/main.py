from string import ascii_uppercase


class Person:

    def __init__(self, name: str, age: int):
        self.verify_name(name)
        self.verify_age(age)

        self._name = name
        self._age = age

    @classmethod
    def verify_name(cls, name):
        if not isinstance(name, str):
            raise TypeError('Wrong name format')
        if name[0] not in ascii_uppercase:
            raise ValueError('Is it really name?')

    @staticmethod
    def verify_age(age):
        if not isinstance(age, int):
            raise TypeError('Wrong age format')
        if not 1 < age < 110:
            raise ValueError(f'Age {age}? Is it really human?!')

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self.verify_age(age)
        self._age = age


class Employee(Person):
    def __init__(self, name, age, profession: str):
        super().__init__(name, age)
        self.verify_profession(profession)

        self._profession = profession

    @staticmethod
    def verify_profession(profession):
        if not isinstance(profession, str):
            raise TypeError('Wrong profession format')
        if profession not in ('engineer', 'software developer'):
            raise ValueError('Change profession, dude =)')

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, profession: str):
        self.verify_profession(profession)


if __name__ == "__main__":
    person = Person('Name', 10)
    person.name = 'Name 1'