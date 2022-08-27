import random
# 내가 입력한 input 조건문
def my_choices():
    mc = input('가위(2)! 바위(1)! 보(0)!: ')
    if mc == '2' or mc =='가위' :
        m_choice = '가위'
    elif mc == '1' or mc =='바위' :
        m_choice = '바위'
    elif mc == '0' or mc == '보'  :
        m_choice = '보'
    else :
        print('다시 입력해주세요!')
        quit()
    return m_choice
# 랜덤 output에 대한 조건문
def random_choice():
    computer = random.randint(0,2)
    if computer == 2:
        choice = '가위'
    elif computer == 1 :
        choice = '바위'
    else :
        choice = '보'
    return choice
# 조건문 정의를 변수에 할당
my_choice = my_choices()
opponent_choice = random_choice()
# 내가 선택한, 랜덤으로 선택된, 결과 출력
print('나의 선택은: {}'.format(my_choice))
print('컴퓨터의 선택은: {}'.format(opponent_choice))
# 결과 비교
if my_choice == '바위' and opponent_choice == '가위' :
    print('내가 승리!')
elif my_choice == '바위' and opponent_choice == '보' :
    print('컴퓨터 승리!')
elif my_choice == '바위' and opponent_choice == '바위' :
    print("비겼어요!")
elif my_choice == '가위' and opponent_choice == '보' :
    print('내가 승리!')
elif my_choice == '가위' and opponent_choice == '바위':
    print('컴퓨터 승리!')
elif my_choice == '가위' and opponent_choice == '가위':
    print("비겼어요!")
elif my_choice == '보' and opponent_choice == '보' :
    print("비겼어요!")
elif my_choice == '보' and opponent_choice == '바위':
    print('내가 승리!')
elif my_choice == '보' and opponent_choice == '가위':
    print('컴퓨터 승리!')
else :
    print('다시 넣어주세요!')