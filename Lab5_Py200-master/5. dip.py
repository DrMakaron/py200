from abc import ABC, abstractmethod
from typing import final


class AbstractChannel(ABC):

    def get_channel_message(self) -> str:
        pass


class AbstractConversation:

    def do_conversation(self) -> list:
        pass


class AbstractCommunicator(ABC):

    def get_channel(self) -> AbstractChannel:
        pass

    @final
    def communicate(self, conversation: AbstractConversation):
        print(*conversation.do_conversation(),
              self.get_channel().get_channel_message(),
              sep = '\n')


class SMSChannel(AbstractChannel):

    def get_channel_message(self) -> str:
        return "(via SMS)"

class SMSCommunicator(AbstractCommunicator):

    def __init__(self):
        self._channel = SMSChannel()

    def get_channel(self) -> AbstractChannel:
        return self._channel


class SimpleCommunicator(AbstractCommunicator):

    def __init__(self, channel: AbstractChannel):
        self._channel = channel

    def get_channel(self) -> str:
        return self._channel


class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_sound(self) -> str:
        pass


class Crow(Bird):

    def do_sound(self) -> str:
        return "Caw"


class Duck(Bird):

    def do_sound(self) -> str:
        return "Quack"


class SimpleConversation(AbstractConversation):

    def __init__(self, bird_1: Bird, bird_2: Bird):
        self.bird_1 = bird_1
        self.bird_2 = bird_2
        self.com = SMSCommunicator()

    def do_conversation(self) -> list:
        sentence1 = f"{self.com.get_channel().get_channel_message()} {self.bird_1.name}: {self.bird_1.do_sound()}, hello {self.bird_2.name}"
        sentence2 = f"{self.com.get_channel().get_channel_message()} {self.bird_2.name}: {self.bird_2.do_sound()}, hello {self.bird_1.name}"
        return [sentence1, sentence2]


bird_1_ = Crow('Jim')
bird_2_ = Duck('Donald Duck')
conv = SimpleConversation(bird_1_, bird_2_)
print(conv.do_conversation())