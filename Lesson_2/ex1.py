def elements_type():
    elements = [1, 'srg', True, 'sekrhvbku', 16.4, None, [10], (2, 2),
                {2: 3, 4: 5}, b'bytes', bytearray(b'hello world!'),
                set('hello'), frozenset('qwerty')]
    for element in elements:
        print(type(element))
    return 0


if __name__ == "__main__":
    elements_type()
