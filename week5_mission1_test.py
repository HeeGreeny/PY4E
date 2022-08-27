import random


def bs31():
    print('--------------------------------')
    print('베스킨~ 라빈스~ ¯\_(ツ)_/¯  31!')
    print('--------------------------------')
    num = 0
    while True:
        try:
            my = input('My turn - space로 구분해서 숫자를 입력해주세요: ')
            s_my = my.split()
            if len(s_my) > 3:
                print('숫자는 1-3회까지 space로 구분해서 입력해주세요')
                continue
            elif not int(s_my[0]) == num + 1:
                print(f'현재 숫자는 {num}입니다. 바로 다음 숫자부터 입력해주세요')
                continue
            elif len(s_my) != 1:
                if not int(s_my[-1]) == int(s_my[-2]) + 1:
                    print('연속된 숫자로 입력해주세요')
                    continue
                elif not int(s_my[1]) == int(s_my[0]) + 1:
                    print('연속된 숫자로 입력해주세요')
                    continue
            elif int(s_my[-1]) > 30 :
                print('당신이 31을 외쳤습니다! 컴퓨터 승!')
                quit()
            num = s_my[-1]
            print('현재 숫자: ', num)

            computer_turn_num = random.randint(1, 3)
            computer_num = []
            for i in range(computer_turn_num):
                num = int(num) + 1
                computer_num.append(num)
                if num < 31:
                    num = computer_num[-1]
                    print('컴퓨터 숫자 :', num)
                elif 31 in computer_num:
                    num == 31
                    print('컴퓨터 숫자 :', num)
                    print('컴퓨터가 31을 외쳤습니다. 당신 승!')
                    quit()
            print('현재 숫자 :', num)
        except ValueError:
            print('숫자를 입력해주세요!')
            exit()


bs31()
