# sample2.py
# simple text editor with undo

class Memento:
    def __init__(self, text):
        self._text = text
    def get_text(self):
        return self._text

class Editor:
    def __init__(self):
        self._text = ""
    def write(self, msg):
        self._text += msg
    def save(self):
        return Memento(self._text)
    def restore(self, memento):
        self._text = memento.get_text()
    def read(self):
        return self._text

if __name__ == '__main__':
    editor = Editor()
    editor.write('Hello ')
    saved = editor.save()
    editor.write('World')
    print('current', editor.read())
    editor.restore(saved)
    print('after undo', editor.read())
