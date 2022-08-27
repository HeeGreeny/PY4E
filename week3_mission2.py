import random
games = int(input('몇 판을 진행하시겠습니까?: '))
#게임진행 조건문
def rsp_advanced(games) :
 win = 0
 lose = 0
 tie = 0
#입력된 게임진행 수만큼 반복문
 for i in range(1,games+1):
#내가 입력한 input 조건문
    def my_choices():
        mc = input('가위(2)! 바위(1)! 보(0)!: ')
        if mc == '2' or mc =='가위' :
            m_choice = '가위'
        elif mc == '1' or mc =='바위' :
            m_choice = '바위'
        elif mc == '0' or mc == '보'  :
            m_choice = '보'
        else :
            print('0,1,2 혹은 가위,바위,보 중에서 입력해주세요!\n')
            return my_choices()
        return m_choice
#랜덤 output에 대한 조건문
    def random_choice():
        choices = ['가위','바위','보']
        chosen_rsp = random.choice(choices)
        return chosen_rsp
#조건문 정의를 변수에 할당
    my_choice = my_choices()
    opponent_choice = random_choice()
#내가 선택한, 랜덤으로 선택된, 결과 출력
    print('나의 선택은: {}'.format(my_choice))
    print('컴퓨터의 선택은: {}'.format(opponent_choice))
#승패 비교
    if my_choice == '바위' and opponent_choice == '가위' :
        print(f'{i}번째 판 내가 승리!\n')
        win +=1
    elif my_choice == '바위' and opponent_choice == '보' :
        print(f'{i}번째 판 컴퓨터 승리!\n')
        lose += 1
    elif my_choice == '가위' and opponent_choice == '보' :
        print(f'{i}번째 판 내가 승리!\n')
        win += 1
    elif my_choice == '가위' and opponent_choice == '바위':
        print(f'{i}번째 판 컴퓨터 승리!\n')
        lose += 1
    elif my_choice == '보' and opponent_choice == '바위':
        print(f'{i}번째 판 내가 승리!\n')
        win += 1
    elif my_choice == '보' and opponent_choice == '가위':
        print(f'{i}번째 판 컴퓨터 승리!\n')
        lose += 1
    elif my_choice == opponent_choice :
        print(f"{i}번째 판 비겼어요!\n")
        tie += 1
    else :
        print('다시 넣어주세요!\n')
    i = i + 1
    continue
#게임결과 비교
 print('나의 전적: {}승 {}무 {}패'.format(win,tie,lose))
 print('컴퓨터의 전적: {}승 {}무 {}패'.format(lose,tie,win))
#메인함수로 최종출력
if __name__ == "__main__" :
    rsp_advanced(games)