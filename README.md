
# Autonomous Vehicle & Robotics Simulation

This project simulates a simple autonomous robot navigating a 2D grid environment using the A* pathfinding algorithm. It demonstrates basic robotic movement, obstacle avoidance, and logging of actions to a separate output file.

## Features

- 2D grid environment with randomly generated obstacles
- A* pathfinding algorithm for efficient path planning
- Simulated robot movement along the computed path
- Logging of simulation steps to an output file (`simulation_output.log`)

## File Structure

Python source code :
autonomous-vehicle-robotics/ autonomous_vehicle_sim.py      # 

Output file with logs from a sample run:
simulation_output.log          # Output file with logs from a sample run 

## Requirements

- Python 3.6+
- No external libraries required (uses only built-in modules)

## Run the simulation

python autonomous_vehicle_sim.py
Run the simulation

python autonomous_vehicle_sim.py


## View Output

Check the simulation_output.log file for the logged movement and pathfinding steps.

## Customize

You can adjust the simulation settings inside the simulate() function in the Python file:

width, height = 20, 10      # Grid size
start = (0, 0)              # Start point
goal = (9, 19)              # Goal point
