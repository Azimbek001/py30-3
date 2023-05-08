# OOP - обьектно ориентированное программирование

class Person :
    head = True

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name},{self.age}'

    def __len__(self):
        return f'len{(self.name)} {self.age}'

person = Person('beka', 19)
person2 = Person('Азимбек',17)
person3 = Person('Руслан',19)
print(person)



