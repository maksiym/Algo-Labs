from lab3.dfs.dfs_path import find_path_by_dfs


def create_from_input_file(input_file_name: str):
    values = []
    xp_values = []
    try:
        with open(input_file_name) as input_file:
            lines = input_file.readlines()
            for line in lines:
                values += line.rstrip().split(' ')
    except FileNotFoundError:
        print('._.')

    values = list(map(int, xp_values))

    graph_ladder = {}

    return graph_ladder


def write_into_output_file(output_file_name: str, result_xp: int) -> None:
    if result_xp <= 0:
        print("No xp!")
    else:
        with open(output_file_name, 'w') as output_file:
            output_file.write(f'{result_xp}')


def main():
    graph_ladder = create_from_input_file('input.txt')

    result_xp_path = find_path_by_dfs(graph_ladder)

    write_into_output_file('output.txt', len(result_xp_path))


if __name__ == '__main__':
    main()
