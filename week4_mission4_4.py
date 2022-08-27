def check_id() :
    # 주민등록번호 입력받기
    while True:
        q1 = input("주민등록번호 앞자리를 넣어주세요: ")
        if (len(q1) != 6) :
            print("다시 확인하시고 넣어주세요(앞 6숫자)")
            continue
        else :
            break
    while True:
        q2 = input("주민등록번호 뒷자리를 넣어주세요: ")
        if (len(q2) != 7) :
            print("다시 확인하시고 넣어주세요(뒷 7숫자)")
            continue
        else :
    # 주민등록번호 유효성검사
             a = int(q1[0]) * 2 + int(q1[1]) * 3 + int(q1[2]) * 4 + int(q1[3]) * 5 + \
                 int(q1[4]) * 6 + int(q1[5]) * 7 + int(q2[0]) * 8 + int(q2[1]) * 9 + \
                 int(q2[2]) * 2 + int(q2[3]) * 3 + int(q2[4]) * 4 + int(q2[5]) * 5
             b = a % 11
             c = 11 - b
             if c > 9:
                c = c - 10
             else:
                 if c == int(q2[6]):
                    print("유효성검사에 통과한 주민등록번호입니다.")
                    print('주민등록번호', q1 + '-' + q2)
                 else:
                    print("유효성검사에 통과하지 못한 주민등록번호입니다.")
                    print('주민등록번호', q1 + '-' + q2)
        break
    # 년,월 + 성별구분 슬라이스
    b_year = q1[:2]
    b_month = q1[2:4]
    gender = q2[0]
    # 성별 조건문
    for n in gender :
        if n == '1' or n == '3':
             s = '남자'
        elif n == '2' or n =='4':
             s = '여자'
        else:
             print('성별을 알 수 없습니다.')
    # 00년 이후 출생자 체크
    if (b_year[0] == '0') or (b_year[0] == '1') or (b_year[0] == '2'):
        while True:
            y = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x: ')
            if (y == 'o' or 'O' or '0') and (gender == '1' or gender == '2'):
                print('잘못된 번호입니다.')
                print('2000년 이후 출생자의 뒷자리 첫숫자는 3 혹은 4 입니다.')
                break
            elif (y == 'o' or 'O' or '0') and (gender == '3' or gender == '4') :
                print(f'{b_year}년{b_month}월 {s}')
                break
            elif (y == 'x' or 'X') :
                print(f'{b_year}년{b_month}월 {s}')
                print('입력된 출생년도가 2000년 이후 입니다. 재확인해주세요.')
                break
            else:
                print('잘못 입력하셨습니다.\n')
                continue
    else :
        if gender == '3' or gender == '4':
            print('잘못된 번호입니다.')
            print('2000년 이전 출생자의 뒷자리 첫숫자는 1 혹은 2 입니다.')
        else :
           print(f'{b_year}년{b_month}월 {s}')
# 결과 출력
check_id()