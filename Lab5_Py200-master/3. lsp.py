from abc import ABC, abstractmethod
from typing import final


class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def do_sound(self) -> str:
        pass


class Crow(Bird):

    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def swim(self):
        raise NotImplementedError("Crows don't swim!")

    def do_sound(self) -> str:
        return "Caw"


class Duck(Bird):

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"


class AbstractConversation:

    def do_conversation(self) -> list:
        pass


# TODO Переделать класс для возможности передачи в него всех объектов типа Птица
class SimpleConversation(AbstractConversation):

    def __init__(self, bird_1: Bird, bird_2: Bird):
        self.bird_1 = bird_1
        self.bird_2 = bird_2

    def do_conversation(self) -> list:
        sentence1 = f"{self.bird_1.name}: {self.bird_1.do_sound()}, hello {self.bird_2.name}"
        sentence2 = f"{self.bird_2.name}: {self.bird_2.do_sound()}, hello {self.bird_1.name}"
        return [sentence1, sentence2]


class Communicator:

    def __init__(self, channel):
        self.channel = channel

    @final
    def communicate(self, conversation: AbstractConversation):
        print(*conversation.do_conversation(),
              f"(via {self.channel})",
              sep='\n')


bird_1_ = Duck('Donald Duck')
bird_2_ = Crow('Jim')
simple_conversation = SimpleConversation(bird_1_, bird_2_)
print(simple_conversation.do_conversation())
