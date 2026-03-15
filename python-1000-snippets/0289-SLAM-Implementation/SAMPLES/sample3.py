# sample3.py
# Simple occupancy grid mapping (mapping-only SLAM) with simulated range readings.

import numpy as np


def bresenham_line(x0, y0, x1, y1):
    """Bresenham line algorithm between two grid cells."""
    x0, y0, x1, y1 = int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1))
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    points = []
    while True:
        points.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return points


def simulate_range(reading_angle, robot_pose, obstacles, max_range=10.0):
    """Simulate a single range measurement in a 2D map with circular obstacles."""
    x, y, theta = robot_pose
    angle = theta + reading_angle
    direction = np.array([np.cos(angle), np.sin(angle)])
    min_dist = max_range
    for (cx, cy, radius) in obstacles:
        # solve ray-circle intersection
        oc = np.array([x - cx, y - cy])
        b = 2 * np.dot(direction, oc)
        c = np.dot(oc, oc) - radius**2
        disc = b**2 - 4 * c
        if disc < 0:
            continue
        t = (-b - np.sqrt(disc)) / 2
        if 0 < t < min_dist:
            min_dist = t
    return min_dist


if __name__ == '__main__':
    np.random.seed(0)

    grid_size = 40
    cell_size = 0.25
    log_odds = np.zeros((grid_size, grid_size))

    # Robot starts near the lower-left of the map
    robot_pose = np.array([2.0, 2.0, np.deg2rad(45)])

    # Define some circular obstacles in world coordinates
    obstacles = [(6.0, 6.0, 1.0), (9.0, 2.0, 0.8)]

    # Beam angles (relative to robot heading)
    beam_angles = np.linspace(-np.pi / 2, np.pi / 2, 9)

    def world_to_grid(p):
        return int(p[0] / cell_size), int(p[1] / cell_size)

    def update_map(pose):
        # Simulate range readings and update log-odds map
        for ang in beam_angles:
            rng = simulate_range(ang, pose, obstacles, max_range=5.0)
            end = pose[:2] + rng * np.array([np.cos(pose[2] + ang), np.sin(pose[2] + ang)])
            cells = bresenham_line(*world_to_grid(pose[:2]), *world_to_grid(end))
            for cell in cells[:-1]:
                x, y = cell
                if 0 <= x < grid_size and 0 <= y < grid_size:
                    log_odds[y, x] -= 0.4  # free space
            # mark endpoint as occupied
            ox, oy = cells[-1]
            if 0 <= ox < grid_size and 0 <= oy < grid_size:
                log_odds[oy, ox] += 1.0

    # Move the robot and update the map
    motions = [(0.5, np.deg2rad(15.0)), (0.5, np.deg2rad(0.0)), (0.5, np.deg2rad(-15.0))]
    for i, (dist, dtheta) in enumerate(motions, start=1):
        robot_pose[2] += dtheta
        robot_pose[0] += dist * np.cos(robot_pose[2])
        robot_pose[1] += dist * np.sin(robot_pose[2])
        update_map(robot_pose)
        print(f"Step {i}: pose = ({robot_pose[0]:.2f}, {robot_pose[1]:.2f}, {np.rad2deg(robot_pose[2]):.1f} deg)")

    # Convert log-odds to occupancy probability
    occupancy = 1 - 1 / (1 + np.exp(log_odds))
    avg_occ = occupancy.mean()
    print(f"\nAverage occupancy probability: {avg_occ:.3f}")

    # Print a small slice of map around the robot
    gx, gy = world_to_grid(robot_pose[:2])
    print("\nMap slice around robot (1=occupied, 0=free):")
    for row in range(max(0, gy - 5), min(grid_size, gy + 5)):
        line = ''
        for col in range(max(0, gx - 5), min(grid_size, gx + 5)):
            prob = occupancy[row, col]
            line += '#' if prob > 0.6 else '.'
        print(line)
