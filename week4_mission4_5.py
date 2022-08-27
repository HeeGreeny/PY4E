def check_id():
    while True:
        q1 = input("주민등록번호 앞자리를 넣어주세요: ")  # 주민등록번호 앞자리 입력받기
        if (len(q1) != 6):
            print("다시 확인하시고 넣어주세요(앞 6숫자)")  # 6숫자를 벗어나는 모든 입력값 체크
            continue
        else:
            if 00 <= int(q1[0:2]) < 23:  # 입력된 2자리 년수로 4자리 년수 추론
                year = 2000 + int(q1[0:2])
            else:
                year = 1900 + int(q1[0:2])
        h_year = int(q1[0:2])  # 년,월,일 슬라이스
        month = int(q1[2:4])
        day = int(q1[4:])
        d31 = [1, 3, 5, 7, 8, 10, 12]  # 올바른 년,월,일 이 입력되었는지 계산(각 년도에 맞는 월의 일수)
        d30 = [4, 6, 9, 11]
        if ((year % 4 == 0 or year % 100 == 0) and year % 400 != 0):
            if (month in d31) and day <= 31 and day >= 1:
                break
            elif (month in d30) and day <= 30 and day >= 1:
                break
            elif (month == 2) and day <= 29 and day >= 1:
                break
            else:
                print('잘못된 생년월일입니다(월과 일을 정확히 넣어주세요)')
                continue
        else:
            if (month in d31) and day <= 31 and day >= 1:
                break
            elif (month in d30) and day <= 30 and day >= 1:
                break
            elif (month == 2) and day <= 28 and day >= 1:
                break
            else:
                print('잘못된 생년월일입니다(월과 일을 정확히 넣어주세요)')
                continue
    while True:
        q2 = input("주민등록번호 뒷자리를 넣어주세요: ")  # 주민등록번호 뒷자리 입력받기
        if len(q2) != 7:
            print("다시 확인하시고 넣어주세요(뒷 7숫자)")  # 7숫자를 벗어나는 모든 입력값 체크
            continue
        elif int(q2[0]) > 4:  # 시작숫자 5부터는 오류메시지 출력
            print('주민등록번호 뒷자리는 1 혹은 2 혹은 3 혹은 4 로 시작됩니다')
            continue
        else:  # 주민등록번호 유효성검사
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

    gender = q2[0]  # 성별 조건문
    for n in gender:
        if n == '1' or n == '3':  # 뒷자리 1,3 은 남자
            s = '남자'
        elif n == '2' or n == '4':  # 뒷자리 2,4 는 여자
            s = '여자'

    if 2000 <= year <= 2022:  # 2000년 이후 출생자 체크
        while True:
            y = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x: ')  # 2000년 이후 출생인지 입력받기
            if y == 'o' and (gender == '1' or gender == '2'):  # input이 o이면서 뒷자리 첫숫자가 1,2인 경우 오류메세지 출력
                print('잘못된 번호입니다.')
                print(f'{year}년 출생자의 뒷자리 첫숫자는 3 혹은 4 입니다.')
                break
            elif y == 'o' and (gender == '3' or gender == '4'):  # input이 o이면서 뒷자리 첫숫자가 3,4인 경우 생년월 과 성별 출력
                print(f'{h_year}년{month}월 {s}')
                break
            elif y == 'x':
                print(f'{h_year}년{month}월 {s}')  # input이 x인 경우 생년월 과 성별 출력 + 오류메세지 출력
                print(f'입력된 출생년도가 {year}년 입니다. 답변을 확인해주세요.')
                break
            else:
                print('잘못 입력하셨습니다.')  # o 또는 x 가 아닌 다른 input 에 오류메세지 출력
                continue
    else:
        if gender == '3' or gender == '4':  # 1900년대 출생자인데 뒷자리 첫숫자가 3,4인 경우 오류메세지 출력
            print('잘못된 번호입니다.')
            print(f'{year}년 출생자의 뒷자리 첫숫자는 1 혹은 2 입니다.')
        else:
            print(f'{h_year}년{month}월 {s}')  # 1900년대 출생자 생년월 과 성별 출력


# # 결과 출력
check_id()