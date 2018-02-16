'''The code for the Histogram Filter. Only the code you write in this file will be graded'''
import pygame
import numpy as np
import math
import random
from scipy import ndimage, spatial
from sklearn import neighbors


class HistogramFilter(object):
    '''Your implementation of a Histogram Filter'''
    def __init__(self, resolution, width, height, landmarks, robot):
        m = int(height / resolution)
        n = int(width / resolution)
        self.belief = np.zeros((m, n)) + (float(1) / (m*n))
        self.landmarks = landmarks
        self.landmarks_tree = neighbors.KDTree([(l.x,l.y) for l in landmarks])
        self.resolution = resolution
        self.z_noise = robot.z_noise
        self.x_noise = robot.x_noise
        self.y_noise = robot.y_noise
        self.phit = robot.phit
        self.pfalse = robot.pfalse
        self.max_sense_dist = robot.max_sense_dist
        self.correspondence_hash = self.setup_correspondence_hash(m,n)

    def setup_correspondence_hash(self, m,n):
        lst = []
        for y in range(int(-1 * self.max_sense_dist - 25), m * self.resolution + (self.max_sense_dist + 25)):
            for x in range(int(-1 * self.max_sense_dist - 25), n * self.resolution + (self.max_sense_dist + 25)):
                lst.append((x,y))
        i = self.landmarks_tree.query(lst, breadth_first=True, return_distance=False)
        h = {}
        for coord, ind in zip(lst, i):
            h[coord] = ind[0]
        return h

    def correspondance(self, potential_x, potential_y, measurements, odom):
        points = [(int(potential_x + x - odom[0]), int(potential_y + (odom[1] - y))) for (x,y) in measurements]
        indices = [ self.correspondence_hash[(x, y)] for (x,y) in points]
        n = len(self.landmarks)
        return [j if j < n else 0 for j in indices]

    def sense_update(self, measurement, odom):
        '''Updates self.belief to reflect the new measurement'''
        # TODO: Insert code here
        pass

    def motion_update(self, odom):
        '''Updates self.belief to reflect the new odometry'''
        # TODO: Insert code here
        pass

    def blit(self, surface, camera):
        '''Draws the histogram to the screen'''
        for i in xrange(self.belief.shape[0]):
            for j in xrange(self.belief.shape[1]):
                x = j * self.resolution
                y = i * self.resolution
                s = pygame.Surface((self.resolution,self.resolution), pygame.SRCALPHA)   # per-pixel alpha
                alpha = 255 * math.sqrt(max(self.belief[i,j], 0)) * 10
                s.fill((255,0,0, min(255, alpha)))                         # notice the alpha value in the color
                surface.blit(s, (x - camera.x, y - camera.y))
