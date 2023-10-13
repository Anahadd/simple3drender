import pygame
import numpy as np
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))

edges = [
    (100, 100, 100), (100, 200, 100), (200, 100, 100), (200, 200, 100),
    (100, 100, 200), (100, 200, 200), (200, 100, 200), (200, 200, 200)
]

center_x = sum([point[0] for point in edges]) / len(edges)
center_y = sum([point[1] for point in edges]) / len(edges)
center_z = sum([point[2] for point in edges]) / len(edges)
center = (center_x, center_y, center_z)

def rotate_point(point, angle):
    px, py, pz = point[0] - center[0], point[1] - center[1], point[2] - center[2]

    angle_rad = math.radians(angle)
    rotation_matrix_y = np.array([
        [math.cos(angle_rad), 0, math.sin(angle_rad)],
        [0, 1, 0],
        [-math.sin(angle_rad), 0, math.cos(angle_rad)]
    ])
    rotated_point = np.dot(rotation_matrix_y, np.array([px, py, pz]))

    return rotated_point + center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    for angle in range(0, 360, 15):
        screen.fill((0, 0, 0))
        for edge in edges:
            rotated_point = rotate_point(edge, angle)
            perspective_scale = 600 / (rotated_point[2] + 600)
            x_proj = rotated_point[0] * perspective_scale
            y_proj = rotated_point[1] * perspective_scale
            pygame.draw.ellipse(screen, (255, 0, 0), (int(x_proj) + 400, int(y_proj) + 400, 5, 5))

        pygame.display.flip()
        pygame.time.wait(100)
