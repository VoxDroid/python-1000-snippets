# sample1.py
# Simple game loop structure demonstrating update and render steps.

import time


class Game:
    def __init__(self, max_frames=10):
        self.max_frames = max_frames
        self.frame = 0
        self.running = True

    def update(self, dt):
        # Update game state (placeholder)
        self.frame += 1
        if self.frame >= self.max_frames:
            self.running = False

    def render(self):
        # Render state (text output for this example)
        print(f"Frame {self.frame}: rendering game state")

    def run(self):
        previous = time.time()
        while self.running:
            current = time.time()
            dt = current - previous
            previous = current
            self.update(dt)
            self.render()
            time.sleep(0.05)


if __name__ == '__main__':
    game = Game(max_frames=5)
    game.run()
