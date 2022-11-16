def play_wchain_game(words_dictionary) -> int:
    max_chain_length = {}
    i = 0
    while i < words_dictionary.__len__():
        max_chain_length[words_dictionary[i]] = 1
        i += 1

    temp = ""
    answer = 0

    words_dictionary.sort(key=len)

    for word in words_dictionary:
        pref = ""
        i = 0
        while i < word.__len__():
            temp = pref
            j = i + 1
            while j < word.__len__():
                temp += word[j]
                j += 1

            if temp in max_chain_length.keys() and max_chain_length[temp] > 0:
                max_chain_length[word] = max(max_chain_length[word], max_chain_length[temp] + 1)

            pref += word[i]
            i += 1

        answer = max(answer, max_chain_length[word])

    return answer


def create_from_input_file(input_file_name: str):
    try:
        with open(input_file_name) as input_file:
            input_lines = input_file.read().splitlines()
    except FileNotFoundError:
        print('._.')

    if int(input_lines[0]) > 10000:
        print("Ooh... max limit of words!")
        return

    return input_lines[1:int(input_lines[0]) + 1]


def write_into_output_file(output_file_name: str, result_max_length: int) -> None:
    if result_max_length <= 0:
        print("No wchain!")
    else:
        with open(output_file_name, 'w') as output_file:
            output_file.write(f'{result_max_length}')


def main():
    words_dictionary = create_from_input_file('resources/wchain.in')
    max_length_wchain = play_wchain_game(words_dictionary)
    write_into_output_file('wchain.out', max_length_wchain)


if __name__ == '__main__':
    main()
