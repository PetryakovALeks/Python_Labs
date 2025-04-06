
import random
import time
#квиз и текстовая игра
r = random.randint(1,2)
point = 0
otvet = input('введите команду')
play = 'играть'
voprosy = 'квиз'
if otvet == play:
    while point < 35:
        print('игра запустилась')
        print('выберите 1 из 3 дверей')
        door = int(input('напишите номер двери(от 1 до 3)'))
        if door == 1:
            print('вы умерли от крысы')
        if door == 2:
            print('вы умерли от зомби')
        if door == 3:
            print('вы нашли сокровище')
            point += 10
            door_1 = int(input('напишите номер двери(от 1 до 2)'))
            if door_1 == 1:
                print('вы унашли монетку')
                point += 5
            if door_1 == 2:
                print('вы найшли груду золота')
                point +=  30
                print('у вас ',point,'монет')
            time.sleep(2)
    print('всего поинтов = ', point)
if otvet ==  voprosy:
    n = str(input('как тебя зовут?'))
    age = int(input('сколько тебе лет?'))
    print('здравствуй, ',n)
    print('сейчас ты будешь учавствовать в квизе по доте)))')
    q1 = input('Сколько скиллов Инвокер может сделать из 3 сфер?')
    if  q1 == '10':
        print('молодец')
        point+= r
        time.sleep(1)
    else:
        print('нет, у него 10 скилов')
        time.sleep(1)
    q2 = input('Сколько всего форм у Tiny?')
    if q2 == '4' or q2 == '3':
        print('молодец')
        point+=r
        time.sleep(1)
    else:
        print('извини но ты не прав их 4')
        time.sleep(1)
    q3 = input('Кто является сильнейшим в лоре Dota 2?')
    if q3 == 'io':
        print('молодец')
        point+=r
        time.sleep(1)
    else:
        print('ты не прав это io')
        time.sleep(1)
    q4 = input('Кто является самой чистой энергией, а кто самый сильный демон?')
    if q4 == 'io и SF':
        print('молодец')
        point+=r
        time.sleep(1)
    else:
        print('как я понял ты не шаришь в этой теме')
        time.sleep(1)    
    q5 = input('как называется сфера огня у инвокера?')
    if q5 == 'exort':
        print('молодец')
        point+=r
        time.sleep(1)
    else:
        print('бро ну это же exort')
        time.sleep(1)
    if q1 == '10' and q5 == 'exort':
        print('200 игр на инвокере не прошли даром))')
        point+=r
        print('вот тебе поинт за знание инвокера')
    else:
        print('ну не пианист ты')
    print('всего поинтов = ', point)
#моя функция(сегодня)
if otvet == 'функция':
    point_me = 0
    point_comp = 0
    c = int(input('сколько игр сыграешь с компьютером?'))
    while c > 0:
        a = input('введите за кого вы будете играть(рыцарь, дракон, принцесса)')
        b = random.randint(1,3)
        c = c - 1
        if b == 1:
            print('компьютер играет за принцессу')
        if b == 2:
            print('компьютер играет за рыцаря')
        if b == 3:
            print('компьютер играет за дракона')
        print('и побеждает...')
        time.sleep(3)
        if a == 'принцесса' and b == 1:
            print('ничья')
        if a == 'рыцарь' and b == 2:
            print('ничья')
        if a == 'дракон' and b == 3:
            print('ничья')
        if a == 'принцесса' and b == 3:
            print('компьютер победил')
            point_comp += 1
        if a == 'рыцарь' and b == 1:
            print('компьютер победил')
            point_comp += 1
        if a == 'дракон' and b == 2:
            print('компьютер победил')
            point_comp += 1
        if a == 'дракон' and b == 1:
            print('ты победил победил')
            point_me += 1
        if a == 'рыцарь' and b == 3:
            print('ты победил победил')
            point_me += 1
        if a == 'принцесса' and b == 2:
            print('ты победил победил')
            point_me += 1
    print('сколько очков набрал компьютер',point_comp)
    print('сколько очков ты набрал ',point_me)
    if point_comp > point_me:
        print('победил во встрече компьютер')
    if point_comp < point_me:
        print('победил во встрече ты')
    if point_comp == point_me:
        print('победила во встрече ничья')