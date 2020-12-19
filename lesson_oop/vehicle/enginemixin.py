from typing import Union

class EngineMixin:
    def prepare(self):
        self.engine.start()

    def sleep(self):
        self.engine.stop()

    def __str__(self):
        output = super().__str__()
        output += f'\n{self.__class__.__name__} characteristics. Engine [{self.engine}]'
        return output
