# sample2.py
# logging level chain

class Logger:
    def __init__(self, level, successor=None):
        self.level = level
        self._successor = successor
    def log(self, level, msg):
        if level == self.level:
            print(f"{self.level}: {msg}")
        elif self._successor:
            self._successor.log(level, msg)

if __name__ == '__main__':
    info = Logger('INFO')
    warn = Logger('WARN', successor=info)
    error = Logger('ERROR', successor=warn)
    error.log('INFO', 'this is info')
    error.log('ERROR', 'this is error')
