def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes


def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        return ' '.join(str(i) for i in range(1,n+1))

if __name__ == "__main__":
    poem = """Stars and the moon
    shine in the sky
    white and
    until the end of the night"""

    poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
    poem3 = 'There\nonce\nwas\na\ndragon'

    print(pin_extractor([poem, poem2, poem3]))

    print(number_pattern(4))