text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl'
        ', facilisis vitae semper at, dignissim vitae libero')
text1 = text.split()
print(text1)
tes = []

for elem in text1:
    if ',' in elem:
        elem = elem.replace(',', 'ing,')
        tes.append(elem)
    elif '.' in elem:
        elem = elem.replace('.', 'ing.')
        tes.append(elem)
    else:
        elem = elem + 'ing'
        tes.append(elem)
print('ddddddddddddddddddddddddddd = ', tes)
