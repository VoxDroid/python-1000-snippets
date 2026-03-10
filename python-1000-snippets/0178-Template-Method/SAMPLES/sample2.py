# sample2.py
# game loop skeleton with hooks

class Game:
    def run(self):
        self.setup()
        for _ in range(3):
            self.update()
            self.render()
        self.cleanup()
    def setup(self):
        print('default setup')
    def update(self):
        pass
    def render(self):
        pass
    def cleanup(self):
        print('default cleanup')

class MyGame(Game):
    def setup(self):
        print('initialize game')
    def update(self):
        print('updating game state')
    def render(self):
        print('rendering frame')

if __name__ == '__main__':
    g = MyGame()
    g.run()
