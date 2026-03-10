# sample3.py
# UI components communicating via mediator

class DialogMediator:
    def __init__(self):
        self.components = {}
    def register(self, name, component):
        self.components[name] = component
        component.mediator = self
    def notify(self, sender, event):
        if sender == 'button' and event == 'click':
            self.components['textbox'].enable()

class Button:
    def __init__(self):
        self.mediator = None
    def click(self):
        print('button clicked')
        self.mediator.notify('button', 'click')

class TextBox:
    def __init__(self):
        self.mediator = None
        self.enabled = False
    def enable(self):
        self.enabled = True
        print('textbox enabled')

if __name__ == '__main__':
    mediator = DialogMediator()
    btn = Button()
    tb = TextBox()
    mediator.register('button', btn)
    mediator.register('textbox', tb)
    btn.click()
