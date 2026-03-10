# sample1.py
# Windows/Mac button example (from existing README)

class Button:
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Windows Button"

class MacButton(Button):
    def render(self):
        return "Mac Button"

class Factory:
    def create_button(self):
        pass

class WindowsFactory(Factory):
    def create_button(self):
        return WindowsButton()

class MacFactory(Factory):
    def create_button(self):
        return MacButton()

if __name__ == '__main__':
    factory = WindowsFactory()
    button = factory.create_button()
    print(button.render())
    factory = MacFactory()
    print(factory.create_button().render())
