import pygame

class Maze(object):
    def __init__(self, x, y, img_path, camera):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(img_path)
        new_width = int(self.sprite.get_width())
        new_height = int(self.sprite.get_height())
        self.sprite = pygame.transform.scale(self.sprite, (new_width, new_height))
        self.camera = camera
        self.mask = pygame.mask.from_threshold(self.sprite, (0,0,0), (127, 127, 127))

    def blit(self, surface):
        surface.blit(self.sprite, (-self.camera.x, -self.camera.y))

    def get_width(self):
        return self.sprite.get_width()

    def get_height(self):
        return self.sprite.get_height()
