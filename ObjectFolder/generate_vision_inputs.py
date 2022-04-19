import math

import numpy
import numpy as np


def circle_points(r, n):
    circles = []
    for r, n in zip(r, n):
        t = np.linspace(0, 2 * np.pi, n, endpoint=False)
        x = r * np.cos(t)
        y = r * np.sin(t)
        circles.append(np.c_[x, y])
    return circles


camera_radius = math.sqrt(3.125)
light_radius = math.sqrt(2) / 2

n_points = 16
points = circle_points([camera_radius], [n_points])[0]
camera_z = np.tile([camera_radius], [n_points, 1])

light_xyz = np.tile([0, -light_radius, light_radius], (n_points, 1))

vision_file_np = np.hstack([points, camera_z, light_xyz])
save_dir = './demo/vision_demo_more.npy'
np.save(save_dir, vision_file_np)
