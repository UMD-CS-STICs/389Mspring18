import pygame
import math
import numpy as np
from random import random

class Camera(object):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.follow_obj = None

    def follow(self, obj):
        self.follow_obj = obj

    def update(self):
        if self.follow_obj:
            self.x = self.follow_obj.x - screen.get_width() / 2
            self.y = self.follow_obj.y - screen.get_height() / 2

class Maze(object):
    def __init__(self, x, y, img_path, camera):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(img_path)
        new_width = self.sprite.get_width() * 20
        new_height = self.sprite.get_height() * 20
        self.sprite = pygame.transform.scale(self.sprite, (new_width, new_height))
        self.camera = camera
        self.mask = pygame.mask.from_threshold(self.sprite, (0,0,0), (127, 127, 127))

    def blit(self, surface):
        surface.blit(self.sprite, (-self.camera.x, -self.camera.y))

    def get_width(self):
        return self.sprite.get_width()

    def get_height(self):
        return self.sprite.get_height()

class Robot(object):
    def __init__(self, x, y, theta, img_path, camera):
        self.x = x
        self.y = y
        self.theta = theta
        self.sprite = pygame.transform.rotate(pygame.image.load(img_path), -90)
        self.sprite_rot = pygame.transform.rotate(self.sprite, math.degrees(theta))
        self.camera = camera
        # self.move(0, 0, None)

    def move(self, dr, dtheta, collision_mask):
        new_theta = self.theta + dtheta
        new_x = self.x + dr * math.sin(new_theta)
        new_y = self.y + dr * math.cos(new_theta)
        new_sprite_rot = pygame.transform.rotate(self.sprite, math.degrees(new_theta))
        mask = pygame.mask.from_surface(new_sprite_rot)
        offsetx = int(new_x - new_sprite_rot.get_width() / 2 + 0.5)
        offsety = int(new_y - new_sprite_rot.get_height() / 2 + 0.5)

        if collision_mask and collision_mask.overlap_area(mask, (offsetx, offsety)) == 0:
            self.x = new_x
            self.y = new_y
            self.theta = new_theta % (2 * math.pi)
            self.sprite_rot = new_sprite_rot

    def blit(self, surface):
        x = self.x - self.sprite_rot.get_width() / 2 - self.camera.x
        y = self.y - self.sprite_rot.get_height() / 2 - self.camera.y
        surface.blit(self.sprite_rot, (x, y))

class Landmark(object):
    def __init__(self, x, y, camera):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.camera = camera

    def blit(self, surface, robot=None):
        x = self.x - self.camera.x
        y = self.y - self.camera.y
        pygame.draw.rect(surface, (0, 255, 0), (x - self.width/2, y - self.height/2, self.width, self.height))
        if robot:
            pygame.draw.line(surface, (0, 0, 255), (x, y), (robot.x - self.camera.x, robot.y - self.camera.y), 2)

pygame.init()
screen = pygame.display.set_mode((1200, 900))
done = False

camera = Camera(screen, 0, 0)
robot = Robot(1670, 1070, math.pi/2, 'car.png', camera)
maze = Maze(0, 0, 'maze.jpg', camera)
camera.follow(robot)

landmarks = [Landmark(random()*maze.get_width(), random()*maze.get_height(), camera) for _ in xrange(1000)]

clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        robot.move(10, 0, maze.mask)
    if pressed[pygame.K_DOWN]:
        robot.move(-10, 0, maze.mask)
    if pressed[pygame.K_LEFT]:
        robot.move(0, math.pi / 20, maze.mask)
    if pressed[pygame.K_RIGHT]:
        robot.move(0, -math.pi / 20, maze.mask)

    camera.update()
    # print '%s, %s, %s' % (robot.x, robot.y, math.degrees(robot.theta))


    screen.fill((255, 255, 255))
    maze.blit(screen)
    robot.blit(screen)
    min_dist = 999999
    for landmark in landmarks:
        dist = math.sqrt((robot.x - landmark.x)**2 + (robot.y - landmark.y)**2)
        if dist < min_dist:
            min_dist = dist
        if 0 < dist < 500:
            landmark.blit(screen, robot=robot)
        else:
            landmark.blit(screen)
    print min_dist
    pygame.display.flip()
    clock.tick(60)
