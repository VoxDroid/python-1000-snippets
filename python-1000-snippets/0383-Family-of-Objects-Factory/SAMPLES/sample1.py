# sample1.py
# Abstract factory producing UI components for different platforms

class Button:
    def render(self):
        raise NotImplementedError


class Checkbox:
    def render(self):
        raise NotImplementedError


class WindowsButton(Button):
    def render(self):
        return "Windows Button"


class MacButton(Button):
    def render(self):
        return "Mac Button"


class WindowsCheckbox(Checkbox):
    def render(self):
        return "Windows Checkbox"


class MacCheckbox(Checkbox):
    def render(self):
        return "Mac Checkbox"


class UIFactory:
    def create_button(self):
        raise NotImplementedError

    def create_checkbox(self):
        raise NotImplementedError


class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


def main():
    factory = WindowsFactory()
    print(factory.create_button().render())
    print(factory.create_checkbox().render())


if __name__ == "__main__":
    main()
