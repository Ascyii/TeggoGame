# The Teggo Game by Jonas Hahn 2021
# This is the main game file
# I will first program everything in here, and
# then I will capsule modules later on
# Afterwards I will implement an online mode and a level editor

# Imports
import pygame
import sys

# Window settings
CAPTION = "Teggo Game 2021"
WIDTH = 500
HEIGHT = 500
FPS = 60
GRID = 64
BACKGROUND_COLOR = "GREEN"

# Initialize pygame
pygame.mixer.init()
pygame.init()


# Define game objects
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x_start, y_start, image):
        super(Sprite, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x_start, y_start


class PassiveObj(Sprite):
    def __init__(self, x_start, y_start, image):
        super(PassiveObj, self).__init__(x_start, y_start, image)


class ActiveObj(Sprite):
    def __init__(self, x_start, y_start, image, vx_init=0, vy_init=0):
        super(ActiveObj, self).__init__(x_start, y_start, image)
        self.vx, self.vy = vx_init, vy_init

    def update_movement(self):
        self.rect.x += self.vx / FPS
        self.rect.y += self.vy / FPS

    def check_for_boundaries(self, width, height):
        if self.rect.left > width:
            self.rect.left = width
        elif self.rect.right < 0:
            self.rect.right = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        elif self.rect.top < 0:
            self.rect.top = 0

    def check_for_obstacles(self, obstacles):
        hit_list = pygame.sprite.spritecollide(self, obstacles, False)
        for hit in hit_list:
            if self.vx > 0:
                self.rect.right = hit.rect.left
            elif self.vx < 0:
                self.rect.left = hit.rect.right
            if self.vy > 0:
                self.rect.top = hit.rect.bottom
            elif self.vy < 0:
                self.rect.bottom = hit.rect.top

    def process_collisions(self, sprites):
        hit_list = pygame.sprite.spritecollide(self, sprites, False)
        for hit in hit_list:
            print(hit)

    def update(self, scene):
        self.check_for_obstacles(scene.obstacles)
        self.check_for_boundaries(scene.width, scene.height)
        self.process_collisions(scene.sprites)
        self.update_movement()


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
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.running = True
        self.scene = Scene()

    def process_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def process_keyboard(self):
        pass

    def process_mouse(self):
        pass

    def process_events(self):
        self.process_exit()
        self.process_keyboard()
        self.process_mouse()

    def update(self):
        for sprite in self.scene.sprites:
            sprite.update()

    def draw(self):
        self.window.fill(BACKGROUND_COLOR)
        self.scene.sprites.draw(self.window)

    def loop(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(FPS)


# Main Function
def main():
    game = Game()
    game.loop()


# Run the main function
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit(1)
