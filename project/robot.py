import pygame
import numpy as np
import math
import random

class RobotBin(object):
    def __init__(self, x, y, img_path, camera, landmarks, negative_landmarks, maze):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(img_path)
        new_width = int(self.sprite.get_width()/2)
        new_height = int(self.sprite.get_height()/2)
        self.sprite = pygame.transform.scale(self.sprite, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.sprite)
        self.camera = camera
        self.x_odom = x
        self.y_odom = y
        self.x_noise = 0.08
        self.y_noise = 0.08
        self.z_noise = 10
        self.phit = 0.9
        self.pfalse = 0.01
        self.max_sense_dist = 100
        self.landmarks = landmarks
        self.negative_landmarks = negative_landmarks
        self.maze = maze

    def blit(self, surface):
        x = self.x - self.sprite.get_width()/2
        y = self.y - self.sprite.get_height()/2
        surface.blit(self.sprite, (x - self.camera.x, y - self.camera.y))
        pygame.draw.rect(surface, (0, 0, 255), (self.x_odom - self.camera.x, self.y_odom - self.camera.y, 10, 10))

    def move(self, dx, dy, collision_mask, tolerance = 0.001):
        if abs(dx) < tolerance and abs(dy) < tolerance:
            return
        new_x = self.x + dx
        new_y = self.y + dy

        offsetx = int(new_x - self.sprite.get_width() / 2 + 0.5)
        offsety = int(new_y - self.sprite.get_height() / 2 + 0.5)

        if collision_mask and collision_mask.overlap_area(self.mask, (offsetx, offsety)) == 0:
            self.x_odom += new_x - self.x + 0.01 + np.random.normal(scale=abs(dx)*self.x_noise) if dx != 0 else 0
            self.y_odom += new_y - self.y + 0.02 + np.random.normal(scale=abs(dy)*self.y_noise) if dy != 0 else 0

            self.x = new_x
            self.y = new_y
        else:
            self.move(dx / 1.5, dy / 1.5, collision_mask)

    def controls(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.move(0, -20, self.maze.mask)
        if pressed[pygame.K_DOWN]:
            self.move(0, 20, self.maze.mask)
        if pressed[pygame.K_LEFT]:
            self.move(-20, 0, self.maze.mask)
        if pressed[pygame.K_RIGHT]:
            self.move(20, 0, self.maze.mask)

    def odometry(self):
        return self.x_odom, self.y_odom

    def detect_landmarks(self):
        detected = []
        for i, landmark in enumerate(self.landmarks):
            dist = math.sqrt((self.x - landmark.x)**2 + (self.y - landmark.y)**2)
            if 0 < dist < self.max_sense_dist and random.random() < self.phit:
                x = self.x_odom + landmark.x - self.x + np.random.normal(scale=self.z_noise)
                y = self.y_odom + landmark.y - self.y + np.random.normal(scale=self.z_noise)
                detected.append((x, y))

        for landmark in self.negative_landmarks:
            dist = math.sqrt((self.x - landmark.x)**2 + (self.y - landmark.y)**2)
            if 0 < dist < self.max_sense_dist and random.random() < self.pfalse:
                x = self.x_odom + landmark.x - self.x + np.random.normal(scale=self.z_noise)
                y = self.y_odom + landmark.y - self.y + np.random.normal(scale=self.z_noise)
                detected.append((x, y))

        return detected

class RobotCar(object):
    def __init__(self, x, y, theta, img_path, camera):
        self.x = x
        self.y = y
        self.theta = theta
        self.sprite = pygame.transform.rotate(pygame.image.load(img_path), -90)
        self.sprite_rot = pygame.transform.rotate(self.sprite, math.degrees(theta))
        self.camera = camera

    def move(self, dr, dtheta, collision_mask, tolerance = 0.001):
        if abs(dr) < tolerance and abs(dtheta) < tolerance:
            return
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
        else:
            self.move(dr / 1.5, dtheta / 1.5, collision_mask)

    def blit(self, surface):
        x = self.x - self.sprite_rot.get_width() / 2 - self.camera.x
        y = self.y - self.sprite_rot.get_height() / 2 - self.camera.y
        surface.blit(self.sprite_rot, (x, y))

    def controls(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.move(10, 0, maze.mask)
        if pressed[pygame.K_DOWN]:
            self.move(-10, 0, maze.mask)
        if pressed[pygame.K_LEFT]:
            self.move(0, math.pi / 20, maze.mask)
        if pressed[pygame.K_RIGHT]:
            self.move(0, -math.pi / 20, maze.mask)
