def play_wchain_game(words_dictionary) -> int:
    pass


def create_from_input_file(input_file_name: str) -> object:
    try:
        with open(input_file_name) as input_file:
            words_dictionary = input_file.read().splitlines()
    except FileNotFoundError:
        print('._.')

    if int(words_dictionary[0]) > 10000:
        print("Ooh... max limit of words!")
        return

    return words_dictionary


def write_into_output_file(output_file_name: str, result_max_length: int) -> None:
    if result_max_length <= 0:
        print("No wchain!")
    else:
        with open(output_file_name, 'w') as output_file:
            output_file.write(f'{result_max_length}')


def main():
    words_dictionary = create_from_input_file('wchain.in')
    max_length_wchain = play_wchain_game(words_dictionary)
    write_into_output_file('wchain.out', max_length_wchain)


if __name__ == '__main__':
    main()
