import heapq
import random
import time

LOG_FILE = "simulation_output.log"

# Logger function to write output to a separate file
def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
    print(message)

# Grid Map and Obstacles
class GridMap:
    def __init__(self, width, height, obstacle_ratio=0.2):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.generate_obstacles(obstacle_ratio)

    def generate_obstacles(self, ratio):
        total_cells = self.width * self.height
        num_obstacles = int(total_cells * ratio)
        for _ in range(num_obstacles):
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.width - 1)
            self.grid[x][y] = 1  # 1 = Obstacle

    def is_free(self, x, y):
        return 0 <= x < self.height and 0 <= y < self.width and self.grid[x][y] == 0

# A* Path Planning
class AStarPlanner:
    def __init__(self, grid):
        self.grid = grid
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def plan(self, start, goal):
        queue = []
        heapq.heappush(queue, (0 + self.heuristic(start, goal), 0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while queue:
            _, cost, current = heapq.heappop(queue)

            if current == goal:
                break

            for move in self.moves:
                next_node = (current[0] + move[0], current[1] + move[1])
                if not self.grid.is_free(*next_node):
                    continue

                new_cost = cost_so_far[current] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(next_node, goal)
                    heapq.heappush(queue, (priority, new_cost, next_node))
                    came_from[next_node] = current

        # Reconstruct path
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from.get(current)
            if current is None:
                log("No path found.")
                return []
        path.append(start)
        path.reverse()
        return path

# Simulated Robot
class Robot:
    def __init__(self, grid, start):
        self.grid = grid
        self.position = start

    def move_along_path(self, path):
        for step in path:
            if self.grid.is_free(*step):
                self.position = step
                log(f"Moved to {step}")
                time.sleep(0.1)
            else:
                log(f"Collision at {step}! Stopping.")
                break

# Main Simulation
def simulate():
    width, height = 20, 10
    start = (0, 0)
    goal = (9, 19)

    grid = GridMap(width, height)
    planner = AStarPlanner(grid)
    robot = Robot(grid, start)

    log("Simulation started.")
    log(f"Planning path from {start} to {goal}...")
    path = planner.plan(start, goal)
    if path:
        log(f"Path found: {path}")
        robot.move_along_path(path)
    else:
        log("Failed to find a path.")
    log("Simulation ended.")

if __name__ == "__main__":
    with open(LOG_FILE, "w"):  # Clear previous output
        pass
    simulate()
