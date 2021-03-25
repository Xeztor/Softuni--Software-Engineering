from abc import ABCMeta, abstractmethod, ABC


class IContent(ABC):
    pass


class MyContent(IContent):
    def __init__(self, content):
        self.content = content

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = ''.join(['<myML>', content, '</myML>'])

    def __repr__(self):
        return self.content


class IEmail(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content

    def __repr__(self):

        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template
#
# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)
