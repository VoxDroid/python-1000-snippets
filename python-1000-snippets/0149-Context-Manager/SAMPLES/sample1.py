# sample1.py
# simple resource manager example

class ResourceManager:
    def __enter__(self):
        print('Resource acquired')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Resource released')

if __name__ == '__main__':
    with ResourceManager():
        print('Using resource')
