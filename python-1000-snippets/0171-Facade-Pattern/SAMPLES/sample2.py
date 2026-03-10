# sample2.py
# home theater subsystem facade

class Amplifier:
    def on(self): print('Amplifier on')
    def off(self): print('Amplifier off')

class DVDPlayer:
    def play(self, movie): print(f'DVD playing {movie}')
    def stop(self): print('DVD stopped')

class Projector:
    def on(self): print('Projector on')
    def off(self): print('Projector off')

class HomeTheaterFacade:
    def __init__(self, amp, dvd, projector):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector
    def watch_movie(self, movie):
        self.amp.on()
        self.projector.on()
        self.dvd.play(movie)
    def end_movie(self):
        self.dvd.stop()
        self.amp.off()
        self.projector.off()

if __name__ == '__main__':
    amp = Amplifier()
    dvd = DVDPlayer()
    proj = Projector()
    theater = HomeTheaterFacade(amp, dvd, proj)
    theater.watch_movie('Inception')
    theater.end_movie()
