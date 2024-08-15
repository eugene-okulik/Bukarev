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
        return (f'Цвет: {self.get_color()} , Длинна стебля: {self.len_stem()},  Цена за 1 шт: {self.price_m()},'
                f' Свежие: {self.fresh()}, Средниее время жизни: {self.evr_l()}, Количество: {self.quantity}')

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


rouse1 = Rouse('70', 'Оранжевый', 50, True, 6, 1, 'Роза1')
rouse2 = Rouse('100', 'Красный', 150, True, 10, 1, 'Роза2')
hydrangea1 = Hydrangea(80, 'Белая', 300, False, 16, 1, 'Гортензия1')


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
        description += f'Название цветка в букете: {self.find()}'
        return description

    def price_b(self):
        return sum(flower.price * flower.quantity for flower in self.flowers)

    def find(self):
        names = [flower.name for flower in self.flowers if (flower.evr_l() == 8) or (flower.evr_l() == 6)
                 or (flower.evr_l() == 1)]
        return ', '.join(names)


bouquet = Bouquet()
bouquet.add_flowers(rouse2)
bouquet.add_flowers(rouse1)
bouquet.add_flowers(hydrangea1)
print(bouquet)
