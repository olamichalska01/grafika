import pygame
import os
import math
from matrix import matrix_multiplication
import keyboard
from scene import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
black, white, blue, red, green, yellow = (
    (20, 20, 20),
    (230, 230, 230),
    (0, 154, 255),
    (255, 0, 0),
    (0, 235, 100),
    (235, 225, 0),
)
width, height = 600, 600

pygame.init()
pygame.display.set_caption("3D cube Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

angle = 0.01
cube_position = [width // 3, height // 3]
scale = 200
points = [n for n in range(32)]

points[0] = [[2], [1], [3]]
points[1] = [[4], [1], [3]]
points[2] = [[4], [4], [3]]
points[3] = [[2], [4], [3]]
points[4] = [[2], [1], [0]]
points[5] = [[4], [1], [0]]
points[6] = [[4], [4], [0]]
points[7] = [[2], [4], [0]]


points[8] = [[-4], [1], [3]]
points[9] = [[-6], [1], [3]]
points[10] = [[-6], [4], [3]]
points[11] = [[-4], [4], [3]]
points[12] = [[-4], [1], [0]]
points[13] = [[-6], [1], [0]]
points[14] = [[-6], [4], [0]]
points[15] = [[-4], [4], [0]]


points[16] = [[2], [1], [-6]]
points[17] = [[4], [1], [-6]]
points[18] = [[4], [4], [-6]]
points[19] = [[2], [4], [-6]]
points[20] = [[2], [1], [-9]]
points[21] = [[4], [1], [-9]]
points[22] = [[4], [4], [-9]]
points[23] = [[2], [4], [-9]]

points[24] = [[-4], [1], [-6]]
points[25] = [[-6], [1], [-6]]
points[26] = [[-6], [4], [-6]]
points[27] = [[-4], [4], [-6]]
points[28] = [[-4], [1], [-9]]
points[29] = [[-6], [1], [-9]]
points[30] = [[-6], [4], [-9]]
points[31] = [[-4], [4], [-9]]

sceneObjects = []
sceneObject1 = SceneObject(points[:8], screen, blue, cube_position, scale)
sceneObject2 = SceneObject(points[8:16], screen, red, cube_position, scale)
sceneObject3 = SceneObject(points[16:24], screen, green, cube_position, scale)
sceneObject4 = SceneObject(points[24:32], screen, yellow, cube_position, scale)
sceneObjects.append(sceneObject1)
sceneObjects.append(sceneObject2)
sceneObjects.append(sceneObject3)
sceneObjects.append(sceneObject4)


def connect_point(i, j, k):
    a = k[i]
    b = k[j]
    pygame.draw.line(screen, black, (a[0], a[1]), (b[0], b[1]), 2)


run = True
while run:
    clock.tick(fps)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for x in sceneObjects:
        x.projectTo2D()

    if keyboard.is_pressed("a"):
        for x in sceneObjects:
            x.moveLeft()
    if keyboard.is_pressed("d"):
        for x in sceneObjects:
            x.moveRight()
    if keyboard.is_pressed("w"):
        for x in sceneObjects:
            x.moveUp()
    if keyboard.is_pressed("s"):
        for x in sceneObjects:
            x.moveDown()
    if keyboard.is_pressed("left"):
        for x in sceneObjects:
            x.rotateLeft(angle)
    if keyboard.is_pressed("right"):
        for x in sceneObjects:
            x.rotateRight(angle)
    if keyboard.is_pressed("up"):
        for x in sceneObjects:
            x.rotateUp(angle)
    if keyboard.is_pressed("down"):
        for x in sceneObjects:
            x.rotateDown(angle)

    pygame.display.flip()

pygame.quit()
