'''
camera.py is used to transform the view such that the car is always in the center.
Do not modify this file
'''
import pygame

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
            self.x = self.follow_obj.x - self.screen.get_width() / 2
            self.y = self.follow_obj.y - self.screen.get_height() / 2
