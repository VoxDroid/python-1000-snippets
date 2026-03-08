# sample2.py
# multiple inheritance with mixins

class LoggerMixin:
    def log(self, msg):
        print(f"LOG: {msg}")

class Data:
    def save(self):
        print("saving data")

class LoggedData(Data, LoggerMixin):
    pass

if __name__ == '__main__':
    ld = LoggedData()
    ld.log('hello')
    ld.save()
