# AI Algorithms in Python

This repository contains Python implementations of various AI algorithms, including A* (A-star), Iterative Deepening Search (IDS), Uniform Cost Search (UCS), and Manhattan Distance heuristic.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms Implemented](#algorithms-implemented)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In the field of Artificial Intelligence (AI), algorithms play a crucial role in problem-solving and decision-making. This repository aims to provide Python implementations of fundamental AI algorithms, allowing developers and enthusiasts to understand, experiment, and utilize these algorithms in their projects.

## Algorithms Implemented

### 1. A* Algorithm

A* (pronounced "A-star") is a popular pathfinding algorithm widely used in various applications, including robotics, video games, and logistics. It efficiently finds the shortest path between two points on a graph, considering both the cost of reaching a node and the estimated cost from the current node to the destination.

### 2. Iterative Deepening Search (IDS)

Iterative Deepening Search is a tree search algorithm that combines the benefits of depth-first search (DFS) and breadth-first search (BFS). It iteratively performs depth-limited searches with increasing depth limits until the goal is found. IDS is particularly useful for searching large state spaces while maintaining low memory requirements.

### 3. Uniform Cost Search (UCS)

Uniform Cost Search is a variant of Dijkstra's algorithm that explores the search space in a breadth-first manner, considering the cost of each path. It always expands the lowest-cost node on the fringe, ensuring that the shortest path to each explored node is found. UCS is suitable for finding the shortest path in weighted graphs with non-negative edge costs.

### 4. Manhattan Distance Heuristic

Manhattan Distance is a heuristic used in various search algorithms, including A* and UCS. It measures the distance between two points on a grid based on the sum of the absolute differences of their coordinates. This heuristic is especially effective in problems where movement is restricted to horizontal and vertical directions, such as puzzle-solving and pathfinding on grid-based maps.

## Usage

To use the algorithms implemented in this repository, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/proplayer5555/Algorithms-AI.git
    ```

2. Navigate to the directory containing the algorithms:

    ```bash
    cd ai-algorithms-python
    ```

3. Choose the algorithm you want to use and run the corresponding Python file:

    ```bash
    python astar.py
    ```

4. Follow the prompts or customize the input parameters as needed for your specific problem.

## Contributing

Contributions to this repository are welcome! If you have suggestions for improvements, bug fixes, or new algorithms to add, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
