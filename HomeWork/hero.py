class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f'Прозвище героя: {self.nickname}, суперспособность: {self.superpower}, здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Bruce Wayne', 'Batman', 'Martial Arts', 120, 'I am the night.')

print(hero.get_name())
hero.double_health()
print(str(hero))
print(len(hero))

