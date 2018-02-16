import pygame
import math
import numpy as np
from random import random
from histfilter import *
from landmark import *
from robot import *
from maze import *
from camera import *

### Initialize graphics ###
pygame.init()
screen = pygame.display.set_mode((1200, 900))
camera = Camera(screen, 0, 0)
maze = Maze(0, 0, 'maze.jpg', camera)
landmarks = [Landmark(random.random()*maze.get_width(), random.random()*maze.get_height(), camera) for _ in xrange(10)]
negative_landmarks = [Landmark(random.random()*maze.get_width(), random.random()*maze.get_height(), camera) for _ in xrange(50)]
robot = RobotBin(34, 263, 'car.png', camera, landmarks, negative_landmarks, maze)
camera.follow(robot)
clock = pygame.time.Clock()

### Initialize Filter ###
hfilter = HistogramFilter(5, maze.get_width(), maze.get_height(), landmarks, robot)


# Loop until QUIT event recieved
while pygame.QUIT not in (event.type for event in pygame.event.get()):

    ### Update World ###
    robot.controls()
    camera.update()

    ### Update Belief ###

    ## Motion Update ##
    odom = robot.odometry()
    hfilter.motion_update(odom)

    ## Measurement Update ##
    detections = robot.detect_landmarks()
    hfilter.sense_update(detections, odom)

    ### Draw World ###
    screen.fill((255, 255, 255))
    maze.blit(screen)
    robot.blit(screen)

    for landmark in landmarks:
        landmark.blit(screen)
    for (x, y) in detections:
        Landmark(x + robot.x - odom[0], y + robot.y - odom[1], camera).blit(screen, robot)

    hfilter.blit(screen, camera)
    pygame.display.flip()
    clock.tick(10)
