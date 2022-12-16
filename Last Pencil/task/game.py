import random


def number_check():
    """return valid input"""
    m_1 = "The number of pencils should be numeric"
    m_1_1 = "The number of pencils should be positive"
    while True:
        k = input()
        if not k.isdigit():
            print(m_1)
        elif int(k) < 0:
            print(m_1)
        elif int(k) == 0:
            print(m_1_1)
        else:
            break
    return k


def player_check_bot(list_of_pl):
    """return tuple - valid player and flag 1 - human, 2 - bot"""
    m_2 = f"Choose between {list_of_pl[0]} and {list_of_pl[1]}"
    while True:
        pl = input()
        if pl not in list_of_pl:
            print(m_2)
        else:
            break
    if pl == list_of_pl[0]:
        flag = 1
    else:
        flag = 2
    return list_of_pl[0], list_of_pl[1], flag


def input_player_number(number):
    m_3 = "Possible values: '1', '2' or '3'"
    m_4 = "Too many pencils were taken"
    values = [1, 2, 3]
    while True:
        d = input()
        if not d.isdigit():
            print(m_3)
        elif int(d) not in values:
            print(m_3)
        elif int(d) > number:
            print(m_4)
        else:
            break
    return d


def main():
    player_1 = "John"
    bot_2 = "Jack"
    list_of_players = [player_1, bot_2]
    print('How many pencils would you like to use:')
    num = int(number_check())
    print(f'Who will be the first ({player_1}, {bot_2}):')
    player, bot, fl = player_check_bot(list_of_players)
    print('|' * num)
    if fl == 1:
        part = player
    else:
        part = bot
    while num:
        print(f"{part}'s turn:")
        if part == player:
            k = input_player_number(num)
            part = bot
        else:
            if num == 1:
                k = 1
            elif (num - 1) % 4 == 0:
                k = random.randrange(1, 4)
            else:
                k = (num - 1) % 4
            part = player
            print(k)
        num = num - int(k)
        if num < 0:
            break
        if num:
            print('|' * num)
    print(part, 'won!')


class Reac:
    def __init__(self, size):
        self.size = size


if __name__ == "__main__":
    main()
