# sample3.py
# switchable GUI factory using runtime config

class Button:
    def click(self):
        pass

class WinButton(Button):
    def click(self):
        return "Win click"

class MacButton(Button):
    def click(self):
        return "Mac click"

class GUIFactory:
    def create_button(self):
        pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

if __name__ == '__main__':
    import os
    theme = os.getenv('THEME', 'win')
    factory = WinFactory() if theme=='win' else MacFactory()
    print(factory.create_button().click())
