# class Azim:
#     loh = "krasava"
#
#     def __init__(self,name,nickname,age):
#         self.name = name
#         self.nickname = nickname
#         self.age = age
#
#     def run(self):
#         return f"я {self.name}"
#     def age(self):
#         return f"мне {self.age}"
#     def nickname (self):
#         return f"мое прозвище {self.nickname}"
#
# class Mirlan(Azim):
#     def __init__(self, name,age,nickname,height):
#         super().__init__(name,age,height)
#         self.height = height
#     def height(self):
#         print(f"{self.name},{self.age},{self.height}")
#
# mirlanchik =Mirlan('Мирлан',18,177)
# Mirlan.height(mirlanchik)

# инкапсуляция
# публичный доступ
# защищенный\приватный
# скрытый
# class Bank:
#     def __init__(self, user, money, key):
#         self._user = user
#         self.money = money
#         self.__key = key
#
#     def set_key(self):
#         return self.__key
#
#     def get_key(self, k):
#         self.__key = k
#
#     def key(self):
#         self._keys()
#
#     def _keys(self):
#         print(self.__key)
#
#     def __str__(self):
#         return f"name is {self._user}\n" \
#                f"money is {self.money}\n" \
#                f"key in #####"
#
#
# k = Bank('beka', 10000000, '12qwer65tre')
#
# print(k.set_key())
# k.get_key('9')
# print(k.set_key())
# k._user = 'Mirlan'
# k.age = 19
# # k.__key = '111111111111'
# k._Bank__key = '1111111'
# k.key()
#
# print(dir(k))

