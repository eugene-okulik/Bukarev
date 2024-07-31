words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
z = '=' * 30


def print_keys(**kwargs):
    for key, value in kwargs.items():
        print(key * value)
        print(z)


print_keys(**words)
