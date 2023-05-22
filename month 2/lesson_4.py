class Mirlan:
    def __init__(self,name,age,height,kg):
        self.name = name
        self.age = age
        self.height = height
        self.kg = kg

    def info(self):
        print(f"Меня зовут {self.name}\n Мне {self.age} лет\n Мой рост {self.height}\n Мой вес {self.kg}")

    def __str__(self):
        return f"{self.name}{self.age}{self.height}{self.kg}"

Informat = Mirlan("Акмаль",16,174,52)
Mirlan.info(Informat)

class Azim(Mirlan):
    def __init__(self,name,age,height,kg,work):
        super().__init__(name, age,height,kg,)
        self.work=work

    def work(self):
       print(f"Я {self.name} люблю жахать {self.work}")

    def __str__(self):
       return f"{self.name} {self.age} {self.height}{self.kg} {self.work}"

akmal =Azim("Атаканов Акмаль",16,174,52,"Бийгазиева Саламата и его ослов",)
Azim.work(akmal)
print("Жопу Ставлю было.")


