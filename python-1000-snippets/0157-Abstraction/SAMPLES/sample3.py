# sample3.py
# abstract property and initializer

from abc import ABC, abstractmethod

class Configuration(ABC):
    @property
    @abstractmethod
    def settings(self):
        pass

class MyConfig(Configuration):
    @property
    def settings(self):
        return {'debug': True}

if __name__ == '__main__':
    cfg = MyConfig()
    print('settings', cfg.settings)
