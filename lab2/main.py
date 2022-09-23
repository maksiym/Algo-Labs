from lab2.bfs.bfs_path import find_path_by_bfs
import random


def create_from_input_file(input_file_name: str):
    parameters = []
    try:
        with open(input_file_name) as input_file:
            lines = input_file.readlines()
            for line in lines:
                parameters += line.rstrip().split(', ')
    except FileNotFoundError:
        print('._.')

    parameters = list(map(int, parameters))
    start_p = (parameters[0], parameters[1])
    destination_p = (parameters[2], parameters[3])

    maze = []
    for i in range(0, parameters[4]):
        i = []
        for j in range(0, parameters[5]):
            i.append(random.randint(0, 1))
        maze.append(i)
        print(i)

    graph_maze = {}
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            graph_maze[(i, j)] = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
            delete = []
            for t in graph_maze[(i, j)]:
                if t[0] < 0 or t[1] < 0 or t[0] > len(maze) - 1 or t[1] > len(maze) - 1:
                    delete.append(t)
            for d in delete:
                graph_maze[(i, j)].remove(d)

    return maze, graph_maze, start_p, destination_p


def write_into_output_file(output_file_name: str, result_length: int) -> None:
    if result_length <= 0:
        print("No path!")
    else:
        with open(output_file_name, 'w') as output_file:
            output_file.write(f'{result_length}')


def main():
    maze, graph_maze, start_p, destination_p = create_from_input_file('input.txt')
    # maze = [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    #         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    #         [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    #         [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    #         [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    #         [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    #         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #         [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    #         [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    #         ]

    result_path = find_path_by_bfs(maze, graph_maze, start_p, destination_p)
    write_into_output_file('output.txt', len(result_path) - 1)

    for i in range(0, len(result_path)):
        if result_path[i] == start_p:
            maze[result_path[i][0]][result_path[i][1]] = "S"
        elif result_path[i] == destination_p:
            maze[result_path[i][0]][result_path[i][1]] = 'D'
        else:
            maze[result_path[i][0]][result_path[i][1]] = '*'

    for i in range(len(maze)):
        print(maze[i])


if __name__ == '__main__':
    main()
