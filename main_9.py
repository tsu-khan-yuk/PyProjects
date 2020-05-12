#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 09.05.2020
#  -> task 1: Допишите класс Unit: добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было
#  установить < 0 (например у юнита осталось 5 здоровья а его ударили на 10)
#  -> task 2: Напишите класс Knight. Реализуйте расчет значения урона для атаки и значения заблокированного
#  урона для защиты. Добавьте в атаку рыцаря игнорирование половины защиты врага.
#  -> task 3: Реализуйте всем классам юнитов в атаке проверку состояния здоровья врага (нельзя атаковать врага,
#  у которого здоровье = 0)
#  -> *task 4: Для мага - продумайте механику использования заклинаний. Вероятнее всего заклинание - обьект
#  отдельного класса (ООП всетаки))))
######################################################################################################################
from PyProjects.Module1 import Mage, Pocket, Item

# todo: прикол со словарями в классах

# example = {
#     "brace": {
#         "defence": 20,
#         "dmg": 30
#     },
#     "sword": {
#         "defence": 40,
#         "dmg": 100
#     },
#     "helmet": {
#         "defence": 100,
#         "dmg": 0
#     }
# }


sword = Item("sword", 10, 100)
shield = Item("shield", 100, 0)

mag = Mage("Sanya", 100, 100)

print(mag)
mag.take_item(sword)
mag.take_item(shield)
print(mag)






