import random
import statistics


# 게임 시작
def guess_numbers():
    number = random.randint(0, 100)
    random_num = []
    for i in range(3):
        while number in random_num:
            number = random.randint(0, 100)
        random_num.append(number)
    ma = max(random_num)
    mi = min(random_num)
    me = statistics.median(random_num)
    print(ma, mi, me)
    chance = 3
    guess_num = []
    while True:
        try:
            for i in range(100):
                print(f'{i+1}차시도')
                g_num = int(input('숫자를 예측해보세요: '))
                if g_num < 0:
                    print('0부터 100 사이의 수를 입력해주세요')
                elif g_num in guess_num:
                    print('이미 예측에 사용한 숫자입니다')
                else:
                    guess_num.append(g_num)

                    if (i+1) % 5 == 0:
                        if g_num in random_num:
                            if g_num == ma:
                                print('숫자를 맞추셨습니다!', g_num, '는 최댓값입니다')
                                chance -= 1
                            elif g_num == mi:
                                print('숫자를 맞추셨습니다!', g_num, '는 최솟값입니다')
                                chance -= 1
                            elif g_num == mi:
                                print('숫자를 맞추셨습니다!', g_num, '는 중간값입니다')
                                chance -= 1

                        if g_num not in random_num:
                            if (g_num < mi) and (mi not in guess_num):
                                print('최솟값은', g_num, '보다 큽니다')
                            elif (g_num > mi) and (mi not in guess_num):
                                print('최솟값은', g_num, '보다 작습니다')
                            elif (g_num > ma) and (ma not in guess_num):
                                print('최대값은', g_num, '보다 작습니다')
                            elif (g_num < ma) and (ma not in guess_num):
                                print('최대값은', g_num, '보다 큽니다')

                    if g_num in random_num:
                        if g_num == ma:
                            print('숫자를 맞추셨습니다!', g_num, '는 최댓값입니다')
                            chance -= 1
                        elif g_num == mi:
                            print('숫자를 맞추셨습니다!', g_num, '는 최솟값입니다')
                            chance -= 1
                        elif g_num == me:
                            print('숫자를 맞추셨습니다!', g_num, '는 중간값입니다')
                            chance -= 1

                    if g_num not in random_num:
                        print(g_num, '는 없습니다')

                    if chance == 0:
                        print('게임종료')
                        print(i+1, '번 시도만에 예측 성공')
                        quit()

        except ValueError:
            print('숫자를 입력해주세요!')
            exit()


guess_numbers()
