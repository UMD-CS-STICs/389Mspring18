import pygame
import numpy as np
from np import linalg as LA
import math
from scipy import ndimage


class HistogramFilter:
    '''Your implementation of a Histogram Filter'''

    def __init__(self, resolution, width, height, landmarks, robot):
        m = int(height / resolution)
        n = int(width / resolution)
        self.belief = np.zeros((m, n)) + (float(1) / (m * n))
        self.landmarks = landmarks
        self.resolution = resolution
        self.z_noise = robot.z_noise
        self.x_noise = robot.x_noise
        self.y_noise = robot.y_noise
        self.phit = robot.phit
        self.pfalse = robot.pfalse
        self.robot = robot

    def sense_update(self, measurement, corr, odom):
        '''Updates self.belief to reflect the new measurement'''
        # TODO: Insert code here
        pass

    def motion_update(self, odom):
        '''Updates self.belief to reflect the new odometry'''
        # TODO: Insert code here
        pass

    def correspondance(self, potential_x, potential_y, measurements):
        corr = []
        for measurement in measurements:
            landmark_index, min_dist = -1, float('inf')
            for i, landmark in enumerate(self.landmarks):
                dist = LA.norm((potential_x + measurement.x - landmark.x,
                                potential_y + measurement.y - landmark.y))
                if dist <= self.robot.max_sense_dist and dist < no_dist:
                    min_dist = dist
                    landmark_index = i
            corr.append((landmark_index, min_dist))
        return corr

    def blit(self, surface, camera):
        '''Draws the histogram to the screen'''
        for i in xrange(self.belief.shape[0]):
            for j in xrange(self.belief.shape[1]):
                x = j * self.resolution
                y = i * self.resolution
                # per-pixel alpha
                s = pygame.Surface(
                    (self.resolution, self.resolution), pygame.SRCALPHA)
                alpha = 255 * math.sqrt(self.belief[i, j]) * 10
                # notice the alpha value in the color
                s.fill((255, 0, 0, min(255, alpha)))
                surface.blit(s, (x - camera.x, y - camera.y))
