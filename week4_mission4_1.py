def check_id() :
    while True:
        q1 = input("주민등록번호 앞자리를 넣어주세요: ")
        if (len(q1) != 6) :
            print("다시 확인하시고 넣어주세요(앞 6숫자)\n")
            continue
        q2 = input("주민등록번호 뒷자리를 넣어주세요: ")
        if (len(q2) != 7) :
            print("다시 확인하시고 넣어주세요(뒷 7숫자)\n")
            continue
        else:
            q = q1 + '-' + q2
            print('주민등록번호',q)
            break

    num = list(q.split('-'))
    b_year = num[0][:2]
    b_month = num[0][2:4]
    gender = num[1][0]
    # b_year = []
    # b_month = []
    # gender = []
    # b_year.append(num[0][:2])
    # b_month.append(num[0][2:4])
    # gender.append(num[1][0])
    print(b_year, b_month, gender)

    for n in gender :
        if n == '1' or n == '3':
             s = '남자'
             print(n)
             print(s)
        elif n == '2' or n =='4':
             s = '여자'
             print(n)
             print(s)
        else:
             print('성별을 알 수 없습니다.')

    if b_year[0] == '0' or b_year[0] == '1' or b_year[0] == '2':
        y = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x: ')
        while True:
            if y == 'o' and (gender == '1' or gender == '2'):
                print('잘못된 번호입니다')
                print('00년생 이후 출생자는 뒷자리 시작숫자가 3 혹은 4 입니다.')
                continue
            elif y == 'o' and (gender == '3' or gender == '4') :
                print(f'{b_year}년{b_month}월 {s}')
                break
            elif y == 'x' :
                print(f'{b_year}년{b_month}월 {s}')
                break
            else:
                print('잘못 입력하셨습니다')
                continue
    else :
        print(f'{b_year}년{b_month}월 {s}')
check_id()