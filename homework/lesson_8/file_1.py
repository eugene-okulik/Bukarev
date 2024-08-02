import random

bonus = bool(random.randrange(0, 2))
salary = int(input('укажите свою зарабатную плату: '))
bonsall = salary + int(random.randrange(0, 100))
if bonus is True:
    print(f"Вы заработали бонус за успешную работу. И ваша зарплата с условиями бонусов составляет:"
          f" {salary},{bonus},-'${bonsall}'")
else:
    print(f"Вы остались без бонусов. Ваша зарплата остается прежней {salary},{bonus}-'${salary}'")
