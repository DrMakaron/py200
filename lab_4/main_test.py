import unittest
from main import Person, Employee


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Name', 10)
        self.employee = Employee('Name', 25, 'software developer')

    def test_name(self):
        self.assertEqual(self.person.name, 'Name')

    def test_wrong_name(self):
        with self.assertRaises(TypeError):
            self.person.verify_name(123)
        with self.assertRaises(ValueError):
            self.person.verify_name('name')

    def test_age(self):
        self.assertEqual(self.person.age, 10)

    def test_wrong_age(self):
        with self.assertRaises(ValueError):
            self.person.verify_age(120)

        with self.assertRaises(TypeError):
            self.person.verify_age('111')

    def test_set_name(self):
        with self.assertRaises(AttributeError):
            self.person.name = 'Nick'

    def test_set_age(self):
        self.person.age = 50
        self.assertEqual(self.person.age, 50)

    def test_profession(self):
        self.assertEqual(self.employee.profession, 'software developer')

    def test_wrong_profession(self):
        with self.assertRaises(ValueError):
            self.employee.verify_profession('')

        with self.assertRaises(TypeError):
            self.employee.verify_profession(132)

    def test_set_profession(self):
        self.employee.profession = 'engineer'
        self.assertEqual(self.employee.profession, 'engineer')


if __name__ == '__main__':
    unittest.main()
