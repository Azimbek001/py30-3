class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase,damage,fly=False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = fly

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f'Прозвище героя: {self.nickname}, суперспособность: {self.superpower}, здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Bruce Wayne', 'Batman', 'Martial Arts', 120, 'I am the night.',50)

print(hero.get_name())
hero.double_health()
print(str(hero))
print(len(hero))

class Airhero(SuperHero):
    element = 'air'

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def fly_true_phrase(self):
        print("Fly in the air")

class Groundhero(SuperHero):
    element = 'ground'

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def fly_true_phrase(self):
        print("Fly in the ground")

air_hero = Airhero('Clark Kent', 'Superman', 'Super Strength', 200, 'Up, up, and away!', 50)
ground_hero = Groundhero('Scott Lang', 'Ant-Man', 'Size Manipulation', 100, 'I am Ant-Man!', 35)
air_hero.double_health()
air_hero.fly_true_phrase()

ground_hero.double_health()
ground_hero.fly_true_phrase()

class Villain(Groundhero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, hero):
        hero.damage **= 2

villain = Villain('Lex Luthor', 'Lex', 'Genius Intellect', 100, 'I am the greatest criminal mind of our time!', 30)
villain.crit(air_hero)
print(air_hero.damage)






