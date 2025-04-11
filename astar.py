from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_positions(grid, target):
    return [
        (i, j)
        for i, row in enumerate(grid)
        for j, val in enumerate(row)
        if val == target
    ]

def astar(grid, start, goal, pass_nodes):
    rows, cols = len(grid), len(grid[0])
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    start_val = grid[start[0]][start[1]]
    goal_val = grid[goal[0]][goal[1]]

    while not frontier.empty():
        _, current = frontier.get()
        if current == goal:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next = (current[0] + dx, current[1] + dy)
            if (
                0 <= next[0] < rows
                and 0 <= next[1] < cols
                and grid[next[0]][next[1]] in [0, start_val, goal_val] + pass_nodes
            ):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    frontier.put((priority, next))
                    came_from[next] = current

    if goal not in came_from:
        return None
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = came_from[curr]
    path.append(start)
    path.reverse()
    return path
