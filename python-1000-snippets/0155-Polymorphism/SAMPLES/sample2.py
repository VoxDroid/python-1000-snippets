# sample2.py
# function accepts any object with a `speak` method

def announce(animal):
    print('Announcing:', animal.speak())

class Bird:
    def speak(self):
        return 'Tweet'

class Robot:
    def speak(self):
        return 'Beep'

if __name__ == '__main__':
    announce(Bird())
    announce(Robot())
