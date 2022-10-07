from lab3.dfs.dfs_path import *


def create_from_input_file(input_file_name: str) -> DFS:
    lines = []
    try:
        with open(input_file_name) as input_file:
            lines = input_file.read().splitlines()
    except FileNotFoundError:
        print('._.')

    height = int(lines[0])
    temp = []

    for i in range(1, len(lines)):
        temp.append(list(map(int, lines[i].split(' '))))

    for t in temp:
        for i in range(0, len(t)):
            t[i] = XPNode(t[i])
    print()

    for i in range(0, len(temp)):
        for j in range(0, len(temp[i])):
            if temp[i][j] == temp[0][0]:
                break
            elif temp[i][j] == temp[i][0]:
                temp[i][j].r_root = temp[i - 1][j]
            elif temp[i][j] == temp[i][-1]:
                temp[i][j].l_root = temp[i - 1][j - 1]
            else:
                temp[i][j].l_root = temp[i - 1][j - 1]
                temp[i][j].r_root = temp[i - 1][j]

    print()

    return temp


def write_into_output_file(output_file_name: str, result_xp: int) -> None:
    if result_xp <= 0:
        print("No xp!")
    else:
        with open(output_file_name, 'w') as output_file:
            output_file.write(f'{result_xp}')


def main():
    temp = create_from_input_file('resources/career.in')
    temp1 = create_from_input_file('resources/career1.in')

    graph_ladder = DFS()
    result_xp_path = graph_ladder.do_xp_nodes(temp)
    result_xp_path1 = graph_ladder.do_xp_nodes(temp1)

    write_into_output_file('career.out', result_xp_path)
    write_into_output_file('career1.out', result_xp_path1)


if __name__ == '__main__':
    main()
