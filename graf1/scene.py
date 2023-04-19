import copy
import pygame
from matrix import matrix_multiplication
import math
import numpy as np


class SceneObject:
    def __init__(self, points, screen, color, cube_position, scale) -> None:
        self.points = points
        self.screen = screen
        self.color = color
        self.cube_position = cube_position
        self.scale = scale

    def projectTo2D(self):
        connectionPoints = []
        index = 0
        stop = False

        for point in self.points:
            distance = 10
            if point[2][0] >= distance:
                stop = True
                break

            z = 1 / (distance - point[2][0])
            projection_matrix = [[z, 0, 0], [0, z, 0]]
            projected_2d = matrix_multiplication(projection_matrix, point)

            x = int(projected_2d[0][0] * self.scale) + self.cube_position[0]
            y = int(projected_2d[1][0] * self.scale) + self.cube_position[1]

            connectionPoints.append([x, y])

            index += 1

        if not stop:
            for m in range(4):
                self.connect_point(m, (m + 1) % 4, connectionPoints)
                self.connect_point(m + 4, (m + 1) % 4 + 4, connectionPoints)
                self.connect_point(m, m + 4, connectionPoints)

    def connect_point(self, i, j, k):
        a = k[i]
        b = k[j]
        pygame.draw.line(self.screen, self.color, (a[0], a[1]), (b[0], b[1]), 2)

    def moveLeft(self):
        for point in self.points:
            point[0][0] = point[0][0] - 0.1

    def moveRight(self):
        for point in self.points:
            point[0][0] = point[0][0] + 0.1

    def moveUp(self):
        for point in self.points:
            point[1][0] = point[1][0] + 0.1

    def moveDown(self):
        for point in self.points:
            point[1][0] = point[1][0] - 0.1

    def rotateDown(self, angle):
        for point in self.points:
            rotation_x = [
                [1, 0, 0],
                [0, math.cos(angle), -math.sin(angle)],
                [0, math.sin(angle), math.cos(angle)],
            ]

            pointNew = matrix_multiplication(rotation_x, point)

            point[0][0] = pointNew[0][0]
            point[1][0] = pointNew[1][0]
            point[2][0] = pointNew[2][0]

        return angle

    def rotateRight(self, angle):
        for point in self.points:
            rotation_y = [
                [math.cos(angle), 0, -math.sin(angle)],
                [0, 1, 0],
                [math.sin(angle), 0, math.cos(angle)],
            ]

            pointNew = matrix_multiplication(rotation_y, point)
            print(pointNew)
            point[0][0] = pointNew[0][0]
            point[1][0] = pointNew[1][0]
            point[2][0] = pointNew[2][0]

        return angle

    def rotateUp(self, angle):
        for point in self.points:
            rotation_x = [
                [1, 0, 0],
                [0, math.cos(angle), math.sin(angle)],
                [0, -math.sin(angle), math.cos(angle)],
            ]

            pointNew = matrix_multiplication(rotation_x, point)

            point[0][0] = pointNew[0][0]
            point[1][0] = pointNew[1][0]
            point[2][0] = pointNew[2][0]

        return angle

    def rotateLeft(self, angle):
        for point in self.points:
            rotation_y = [
                [math.cos(angle), 0, math.sin(angle)],
                [0, 1, 0],
                [-math.sin(angle), 0, math.cos(angle)],
            ]

            pointNew = matrix_multiplication(rotation_y, point)
            print(pointNew)
            point[0][0] = pointNew[0][0]
            point[1][0] = pointNew[1][0]
            point[2][0] = pointNew[2][0]

        return angle

    def is_point_visible(self, point_3d, focal: float) -> bool:
        print(point_3d[1][0])
        return point_3d[1][0] > focal
