# Создайте программу для игры в ""Крестики-нолики"".
import random
import emoji
gamer1 = input('Введите имя первого игрока: ')
gamer2 = input('Введите имя второго игрока: ')

# формируем очередность игроков
list_gamers = [gamer1, gamer2]
list_gamers[0] = random.choice(list_gamers)
if list_gamers[0] == gamer1:
    list_gamers[1] = gamer2
else:
    list_gamers[1] = gamer1
print(
    'Играют в Крестики-нолики: ', gamer1, ' и ', gamer2, '.\n'
    'Первым будет ходить - ', list_gamers[0], ' - X\n'
    'Вторым будет ходить - ', list_gamers[1], ' - 0\n'
)
print('На поле указаны координаты ячеек:')
print(
    '-------\n'
    '|1|2|3|\n'
    '-------\n'
    '|4|5|6|\n'
    '-------\n'
    '|7|8|9|\n'
    '-------\n'
)
# функция для отрисовки сетки
def draw_grid(l1):
    print('-------')
    print("|{}|{}|{}|".format(l1[0], l1[1], l1[2]))
    print('-------')
    print("|{}|{}|{}|".format(l1[3], l1[4], l1[5]))
    print('-------')
    print("|{}|{}|{}|".format(l1[6], l1[7], l1[8]))
    print('-------')

# определяем, не случилась ли победа
def check_win(l2, temp):
    if temp%2 == 0: elem = '0'
    else: elem = 'X'
    for i in (0, 3, 6): 
        if (l2[i] == elem and l2[i+1] == elem and l2[i+2] == elem): return True
    for i in (0, 1, 2):         
        if (l2[i] == elem and l2[i+3] == elem and l2[i+6] == elem): return True
    if (l2[0] == elem and l2[4] == elem and l2[8] == elem): return True
    if (l2[2] == elem and l2[4] == elem and l2[6] == elem): return True
        
# играем
listXO = []
for i in range(0, 9):
    listXO.append(' ')
move_g = 0
while check_win(listXO, move_g) != True:
    print('Ход', move_g+1, '- Игрок', list_gamers[move_g % 2])
    print('Введите координату ячейки: ')
    coord = int(input())
    if move_g % 2 == 0:
        listXO[coord-1] = 'X'
    else:
        listXO[coord-1] = '0'
    draw_grid(listXO)
    move_g += 1
print('Победил игрок', list_gamers[move_g % 2 -1], emoji.emojize(':thumbs_up:'))