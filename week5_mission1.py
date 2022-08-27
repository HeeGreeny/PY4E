import random


# 게임 시작
def bs31():
    print('--------------------------------')
    print('베스킨~ 라빈스~ ¯\_(ツ)_/¯  31!')
    print('--------------------------------')
# 첫숫자가 num+1이 될수 있게 0으로 시작
    num = 0
    while True:
        try:
            my = input('My turn - space로 구분해서 숫자를 입력해주세요: ')
            # 입력값 공백 기준으로 슬라이스
            s_my = my.split()
            # 입력값은 총 3회까지 가능
            if len(s_my) > 3:
                print('숫자는 1-3회까지 space로 구분해서 입력해주세요')
                continue
            # 첫숫자는 1부터 시작 혹은 현재숫자+1
            elif not int(s_my[0]) == num + 1:
                print(f'현재 숫자는 {num}입니다. 바로 다음 숫자부터 입력해주세요')
                continue
            # 입력값이 1회 이상일때
            elif len(s_my) != 1:
                # 마지막 입력값은 바로 전 입력값+1
                # if not int(s_my[-1]) == int(s_my[-2]) + 1:
                if not len(s_my) - 1 == len(s_my) - 2:
                    print('연속된 숫자로 입력해주세요')
                    continue
                # 2번째 입력값은 1번째 입력값+1
                # elif not int(s_my[1]) == int(s_my[0]) + 1:
                # elif not len(s_my)  == len(s_my) + 1:
                #     print('연속된 숫자로 입력해주세요')
                #     continue
            # 마지막 입력값을 현재숫자로 지정
            num = s_my[-1]
            print('현재 숫자: ', num)
            # 마지막 입력값이 31이상이면 게임 끝!
            if int(s_my[-1]) > 30:
                print('당신이 31을 외쳤습니다! 컴퓨터 승!')
                quit()
            # 컴퓨터 랜덤으로 3회까지 숫자츌룍
            computer_turn_num = random.randint(1, 3)
            # 출력된 숫자 넣을 리스트 만들어두기
            computer_num = []
            # 출력된 숫자 순서대로 반복
            for i in range(computer_turn_num):
                # 첫숫자는 현재숫자+1 이여야 함
                num = int(num) + 1
                # 출력된 숫자 리스트에 추가
                computer_num.append(num)
                # 출력된 숫자가 31이하 이면 마지막 출력값을 현재숫자에 지정
                if num < 31:
                    num = computer_num[-1]
                    print('컴퓨터 숫자 :', num)
                # 출력된 숫자중 31이 포함되면 현재숫자는 31이 되고 게임종료!
                elif 31 in computer_num:
                    num == 31
                    print('컴퓨터 숫자 :', num)
                    print('컴퓨터가 31을 외쳤습니다. 당신 승!')
                    quit()
            print('현재 숫자 :', num)
        # 숫자가 아닌 입력값은 오류처리
        except ValueError:
            print('숫자를 입력해주세요!')
            exit()


bs31()
