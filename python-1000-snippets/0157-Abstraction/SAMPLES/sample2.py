# sample2.py
# attempting to instantiate abstract class raises TypeError

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

if __name__ == '__main__':
    try:
        a = Animal()
    except TypeError as e:
        print('error', e)
    
    class Dog(Animal):
        def speak(self):
            return 'woof'
    d = Dog()
    print('dog says', d.speak())
