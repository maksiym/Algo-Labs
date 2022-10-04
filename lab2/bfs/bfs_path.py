from collections import deque


def find_path_by_bfs(maze: list, graph: dict, start_point: tuple, destination_point: tuple) -> list:
    search_queue = deque()
    is_path = False
    search_queue.append(start_point)
    n_checked = [start_point]
    checked = []
    prev_neighbour = {start_point: None}

    while search_queue:

        curr_point = search_queue.popleft()
        neighbours = graph[curr_point]

        if curr_point not in checked:

            if destination_point in neighbours:
                prev_neighbour[destination_point] = curr_point
                is_path = True
                break

            else:

                for n in neighbours:
                    if n not in n_checked:
                        if maze[n[0]][n[1]] == 1:
                            prev_neighbour[n] = curr_point
                            search_queue.append(n)
                        n_checked.append(n)
                checked.append(curr_point)

    shortest_path = [destination_point]
    if is_path:
        while prev_neighbour[destination_point] is not None:
            shortest_path.append(prev_neighbour[destination_point])
            destination_point = prev_neighbour[destination_point]
        # shortest_path.reverse()

    return shortest_path
