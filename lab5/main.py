def do_rabin_karp(pattern, text, q=101, d=256):
    pattern_length = len(pattern)
    text_length = len(text)
    p_hash = 0
    t_hash = 0
    hash_value = 1
    i = 0
    j = 0
    match_idx = []

    for i in range(pattern_length - 1):
        hash_value = (hash_value * d) % q

    for i in range(pattern_length):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(text_length - pattern_length + 1):
        if p_hash == t_hash:
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    break

            j += 1
            if j == pattern_length:
                match_idx.append(i)

        if i < text_length - pattern_length:
            t_hash = (d * (t_hash - ord(text[i]) * hash_value) + ord(text[i + pattern_length])) % q

            if t_hash < 0:
                t_hash = t_hash + q
    return match_idx


def main():
    pattern = ""
    text = ""
    do_rabin_karp(pattern, text)


if __name__ == '__main__':
    main()
