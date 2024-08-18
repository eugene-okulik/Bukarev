class Flowers:

    def __init__(self, stem, color, price, freshness, evr_life, quantity, name):
        self.stem = stem
        self.color = color
        self.price = price
        self.freshness = freshness
        self.evr_life = evr_life
        self.quantity = quantity
        self.name = name

    def get_color(self):
        if self.color:
            return self.color
        else:
            return 'цвет не определен'

    def fresh(self):
        if self.freshness:
            return 'Свежие'
        else:
            return 'Не свежие'

    def len_stem(self):
        if self.stem:
            return self.stem
        else:
            return 'длинна стебля не указана'

    def price_m(self):
        if self.price:
            return self.price
        else:
            return 'Цена не указана'

    def evr_l(self):
        if self.fresh() == 'Свежие':
            return self.evr_life
        else:
            return self.evr_life / 2

    def __str__(self):
        return (f'Название цветка: {self.name}, Цвет: {self.get_color()} ,'
                f' Длинна стебля: {self.len_stem()},  Цена за 1 шт: {self.price_m()},'
                f' Свежие: {self.fresh()}, Средниее время жизни: {self.evr_l()},'
                f' Количество: {self.quantity}')

    def name_r(self):
        if self.name:
            return self.name
        else:
            return 'имя не определено'


class Rouse(Flowers):
    def __init__(self, stem, color, price, freshness, evr_life, quantity, name):
        super().__init__(stem, color, price, freshness, evr_life, quantity, name)


class Hydrangea(Flowers):
    def __init__(self, stem, color, price, freshness, evr_life, quantity, name):
        super().__init__(stem, color, price, freshness, evr_life, quantity, name)


rouse1 = Rouse(60, 'Оранжевый', 50, True, 6, 1, 'Роза1')
rouse2 = Rouse(50, 'Красный', 150, True, 10, 1, 'Роза2')
hydrangea1 = Hydrangea(2, 'Белая', 300, True, 8, 1, 'Гортензия1')
hydrangea2 = Hydrangea(4, 'Белая', 300, False, 15, 1, 'Гортензия2')
hydrangea3 = Hydrangea(40, 'Белая', 300, True, 15, 1, 'Гортензия3')


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)

    def aver_rip(self):
        lifetime_all = sum(flower.evr_l() * flower.quantity for flower in self.flowers)
        q_all = sum(flower.quantity for flower in self.flowers)
        return lifetime_all / q_all if q_all != 0 else 0

    def __str__(self):
        description = 'Букет состоит из следующих цветов:\n'
        for flower in self.flowers:
            description += f'{flower}\n'
        description += f'Среднее время жизни букета: {self.aver_rip()} дней.\n'
        description += f'Стоимость букета составляет: {self.price_b()} \n'
        description += f'Название цветка в букете: \n{self.find}'
        return description

    def price_b(self):
        return sum(flower.price * flower.quantity for flower in self.flowers)

    def find(self, list_1):
        result = []
        for flower in self.flowers:
            if flower.evr_l() in list_1:
                result.append(flower)
        return result

    def bubble_sort(self, key_func):
        n = len(self.flowers)
        for i in range(n):
            for flower in range(0, n - i - 1):
                if key_func(self.flowers[flower]) > key_func(self.flowers[flower + 1]):
                    self.flowers[flower], self.flowers[flower + 1] = self.flowers[flower + 1], self.flowers[flower]

    def sort_by_freshness(self):
        def freshness_key(flower):
            return 0 if flower.freshness else 1
        self.bubble_sort(freshness_key)

    def sort_by_color(self):
        def color_key(flower):
            return flower.color
        self.bubble_sort(color_key)

    def sort_by_stem_length(self):
        def stem_key(flower):
            return flower.stem
        self.bubble_sort(stem_key)

    def sort_by_price(self):
        def price_key(flower):
            return flower.price
        self.bubble_sort(price_key)


bouquet = Bouquet()


bouquet.add_flowers(rouse2)
bouquet.add_flowers(rouse1)
bouquet.add_flowers(hydrangea1)
bouquet.add_flowers(hydrangea2)
bouquet.add_flowers(hydrangea3)


print(bouquet)
found_flowers = bouquet.find([6, 8, 10, 15])
for flower in found_flowers:
    print(flower)
