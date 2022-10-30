import numpy as np

class Player():
    def __init__(self,name,is_human):
        self.my_field = []
        self.name = name
        self.is_human = is_human
        self.create_field()

    def __str__(self):
        if self._is_human:
            return f'It is unique player'
        else:
            return f'It is PC'

    def __eq__(self, other):
        return self.name == other.name and self.is_human == other.is_human

    @property
    def is_human(self):
        return self._is_human

    @is_human.setter
    def is_human(self,is_human):
        if isinstance(is_human,bool):
            self._is_human = is_human
        else:
            raise (ValueError)

    def create_field(self):
        # Создание первой строки
        first_str = list(set(np.random.choice([1,2,3,4,5,6,7,8,9],size = 5)))
        np.random.shuffle(first_str)
        self.my_field.extend(map(str,first_str))
        self.my_field.extend(['0']*(9-len(first_str)))
        # Создание остальных строк
        prefix_str = ['1','2','3','4','5','6','7','8','9']
        for num_str in range(2):
            np.random.shuffle(prefix_str)
            field = []
            for elem in prefix_str[:5]:
                field.append(elem + str(np.random.randint(10)))
            field.extend(['0'] * 4)
            np.random.shuffle(field)
            self.my_field.extend(field)
        for k in range(2):
            for i in range(3):
                for j in range(9):
                    try:
                        if int(self.my_field[i*9+j]) > 0:
                            self.my_field[i*9 + int(self.my_field[i * 9 + j][0]) - 1], self.my_field[i*9+j] = self.my_field[i*9+j], self.my_field[i*9 + int(self.my_field[i * 9 + j][0]) - 1]
                    except:
                        pass


    def print_field(self):
        size = (3,9)
        print('*' * size[1] * 4)
        print(f'Поле игрока: {self.name}')
        print('*' * size[1] * 4)
        for i in range(size[0]):
            print(' ',end = '')
            for j in range(size[1]):
                #if self.my_field[i*size[1]+j] != 0:
                z = '_'
                if self.my_field[i*size[1]+j] == '0':
                    print('{:4}'.format(z), end='')
                else:
                    print('{:4}'.format(self.my_field[i*size[1]+j]),end = '')
            print()
        print('*'*size[1]*4)

    def fill_field(self,num):
        # Заполнение хода
        for i in np.where(np.array(list(map(int,self.my_field))) == num)[0]:
            self.my_field[i] = '0'

        # Проверка на конец игры
        return True if np.where(np.array(list(map(int, self.my_field))) == 0)[0].shape[0] == 27 else False

def _user_int_input_(ot = 1, do = 100, entrance_message = 'Ввод:'):
    correct_input = False
    while correct_input == False:
        try:
            _input = int(input(entrance_message))
        except:
            print('Введено неверное знчение')
        else:
            if _input > ot and _input <do:
                correct_input = True
            else:
                print(f'Данное число не удовлетворяет диапазону от {ot} до {do}. Повторите ввод...')
    return _input

if __name__ == '__main__':
    count_players = _user_int_input_(ot = 1, do = 24, entrance_message = 'Введите количество игроков:')

    count = 0
    players_format = []
    print('Введите через пробел "Pl" для добавления игрока и "PC" для добавления бота:')
    while count != count_players:
        print(f'Введите ещё {count_players-count} игроков:')
        input_players = input()
        for i in input_players.split(' '):
            if len(players_format) < count_players:
                if i == 'Pl':
                    players_format.append(True)
                elif i == 'PC':
                    players_format.append(False)
        count = len(players_format)
    print(players_format)

    players = []
    for i in range(len(players_format)):
        players.append(Player(i+1,players_format[i]))

    for player in players:
        player.print_field()
    win = False
    print('Начало игры!')
    while win != True:
        game_number = np.random.randint(1,high=99)
        print(game_number)
        for player in players:
            print(f'Ход игрока {player.name}')
            if player.is_human:
                print('Есть ли у вас нужное число?\n1 - Да\n2 - Нет')
                x = 0
                while x != '1' and x != '2':
                    x = input()
                    if x != '1' and x != '2':
                        print('Неверный ввод')

            if game_number in list(map(int,player.my_field)):
                if player.is_human:
                    if x == '2':
                        print(f'Игрок {player.name} выходит из игры')
                    else:
                        print(f'Игрок {player.name} может закрывает поле {game_number}')
                        win = player.fill_field(game_number)
                else:
                    print(f'Игрок {player.name} может закрывает поле {game_number}')
                    win = player.fill_field(game_number)

                if win == True:
                    print(f'Победил игрок {player.name}')
                    break
        for player in players:
            player.print_field()