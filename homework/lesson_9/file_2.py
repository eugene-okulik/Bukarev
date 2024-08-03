temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]


def hot_days(x):
    if x > 28:
        return x


new_hot_days = filter(hot_days, temperatures)
hot = list(filter(lambda x: x if x > 28 else False, temperatures))
print(hot)
print('Минимальное значение температуры = ', min(hot))
print('Максимальное значение температуры = ', max(hot))
print('Среднее значение температуры = ', sum(hot) / len(hot))
