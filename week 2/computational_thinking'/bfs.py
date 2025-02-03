## algorith that searches the graph data  
from collections import deque

def bfs_short_path(graph, start, goal):
    start = 0

    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path   ## found it
        
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)


        return None       # no path found       

'''
example_graph = ('./graph.txt')

start_node = 'A' 
goal_node = 'F'

path = bfs_short_path(example_graph, start_node, goal_node)

print(f'shortest path from {start_node} to {goal_node}: {path}')'''


def main():
    example_graph = ('./graph.txt')

    start_node = 'A' 
    goal_node = 'F'

    path = bfs_short_path(example_graph, start_node, goal_node)

    if path is True:
        print(f'shortest path from {start_node} to {goal_node}: {path}')

    else:
        print('no path found')


if __name__ == "__main__":
    main()

