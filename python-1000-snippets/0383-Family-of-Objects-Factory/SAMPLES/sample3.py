# sample3.py
# Use a factory selector that chooses the concrete factory at runtime

class UIFactory:
    def create_button(self):
        raise NotImplementedError


class WindowsButton:
    def render(self):
        return "Windows Button"


class MacButton:
    def render(self):
        return "Mac Button"


class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()


class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()


def get_factory(platform):
    if platform == "windows":
        return WindowsFactory()
    return MacFactory()


def main():
    factory = get_factory("mac")
    print(factory.create_button().render())


if __name__ == "__main__":
    main()
