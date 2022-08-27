import random
import statistics


def guess_numbers():
    # 0~100 랜덤숫자 추출
    number = random.randint(0, 100)
    # 추출된 랜덤숫자 리스트화
    random_num = []
    # 중복없는 총 3개의 랜덤숫자 추출
    for i in range(3):
        while number in random_num:
            number = random.randint(0, 100)
        random_num.append(number)
    # 최솟값, 중간값, 최대값 추출
    ma = max(random_num)
    mi = min(random_num)
    me = statistics.median(random_num)
    # 3개 정답 설정
    chance = 3
    # 입력받은 예측숫자 리스트화
    guess_num = []
    while True:
        try:
            for i in range(100):
                # 시도한 차수 출력
                print(f'{i+1}차시도')
                # 시도 입력 받기
                g_num = int(input('숫자를 예측해보세요: '))
                # 0~100 넘어간 숫자입력시 오류 출력
                if g_num < 0:
                    print('0부터 100 사이의 수를 입력해주세요')
                # 중복된 숫자입력시 오류 출력
                elif g_num in guess_num:
                    print('이미 예측에 사용한 숫자입니다')
                else:
                    guess_num.append(g_num)
                    # 시도한 차수가 5의 배수인 경우
                    if (i+1) % 5 == 0:
                        # 입력된 숫자가 정답인 경우 메세지 출력 및 정답수 3에서 1 빼기
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
                        # 시도한 차수가 5의 배수일때 힌트 출력
                        if g_num not in random_num:
                            # 아직 최솟값이 입력되지 않은 경우에는 최솟값 힌트를 보여줌
                            if (g_num < mi) and (mi not in guess_num):
                                print('최솟값은', g_num, '보다 큽니다')
                            elif (g_num > mi) and (mi not in guess_num):
                                print('최솟값은', g_num, '보다 작습니다')
                            # 이미 최솟값이 입력된 경우에는 최대값 힌트를 보여줌
                            elif (g_num > ma) and (ma not in guess_num):
                                print('최대값은', g_num, '보다 작습니다')
                            elif (g_num < ma) and (ma not in guess_num):
                                print('최대값은', g_num, '보다 큽니다')
                    # 5의 배수가 아닌 모든 차수의 경우
                    if g_num in random_num:
                        # 입력된 숫자가 정답인 경우 메세지 출력 및 정답수 3에서 1 빼기
                        if g_num == ma:
                            print('숫자를 맞추셨습니다!', g_num, '는 최댓값입니다')
                            chance -= 1
                        elif g_num == mi:
                            print('숫자를 맞추셨습니다!', g_num, '는 최솟값입니다')
                            chance -= 1
                        elif g_num == me:
                            print('숫자를 맞추셨습니다!', g_num, '는 중간값입니다')
                            chance -= 1
                    # 입력된 숫자가 정답이 아닌 경우 메세지 출력
                    if g_num not in random_num:
                        print(g_num, '는 없습니다')
                    # 정답수 3개를 모두 맞추면 시도 차수 메시지 출력 및 게임 종료
                    if chance == 0:
                        print('게임종료')
                        print(i+1, '번 시도만에 예측 성공')
                        quit()
        # 입력된 값이 숫자가 아닌 경우
        except ValueError:
            print('숫자를 입력해주세요!')
            exit()


guess_numbers()
