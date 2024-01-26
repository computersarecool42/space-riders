import sys
import pygame


class Game:
    def __init__(self):
        self.text = None
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.font = pygame.font.Font(None, 30)

    def update_screen(self):
        self.screen.fill((0, 0, 230))
        self.screen.blit(self.text, (50, 50))
        pygame.display.flip()

    def eprint(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.text = self.font.render('Key code: ' + str(event.key), True, (255,255,255))




    def run(self):
        while True:
            self.update_screen()
            self.eprint()


if __name__ == '__main__':
    new = Game()
    new.run()