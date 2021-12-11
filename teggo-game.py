# The Teggo Game by Jonas Hahn 2021
# This is the main game file
# I will first program everything in here, and
# then I will capsule modules later on

# Imports
import pygame
import sys

# Window settings
CAPTION = "Teggo Game 2021"
WIDTH = 500
HEIGHT = 500
FPS = 60
BACKGROUND_COLOR = "GREEN"

# Initialize Pygame
pygame.mixer.init()
pygame.init()
pygame.display.set_caption(CAPTION)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame_clock = pygame.time.Clock()


# Define game objects
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x_start, y_start, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x_start, y_start

        self.vx = 0
        self.vy = 0


# Scene manager class
class Scene:
    def __init__(self):
        self.sprites = pygame.sprite.Group()

    def load_images(self):
        pass

    def reset(self):
        pass

    def change(self):
        pass


# Game manager class
class Game:
    def __init__(self):
        self.running = True
        self.scene = Scene()

    def process_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def process_events(self):
        self.process_exit()

    def update(self):
        pass

    def draw(self):
        window.fill(BACKGROUND_COLOR)
        self.scene.sprites.draw(window)

    def loop(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()

            pygame.display.update()
            pygame_clock.tick(FPS)


# Main Function
def main():
    game = Game()
    game.loop()


# Run the main function
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit(1)
