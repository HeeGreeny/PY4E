def gender(q2):
    if q2.startswith('2' or '4'):
        s = '여자'
        print(s)
    elif q2.startswith('1' or '3'):
        s = '남자'
        print(s)
    else:
        print('성별을 알 수 없습니다.')
    return

def birth(q):
    num = list(q.split('-'))
    b_year = []
    b_month = []
    b_year.append(num[0][:2])
    b_month.append(num[0][2:4])
    print(b_year,b_month)
    return

# def check_id(q1,q2,s,b_year,b_month) :
#     while q1.startswith('0' or '1' or '2'):
#         y = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x')
#         if y == 'o' and q2.startswith('1'or'2') :
#             print('질못된 번호입니다.')
#         elif y == 'o' and q2.startswith('3'or'4') :
#             print(f'{b_year}년{b_month}월 {s}')
#         else :
#             print(f'{b_year}년{b_month}월 {s}')
#             break


def main() :
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
    gender(q2)
    birth(q)

if __name__ == "__main__" :
    main()

def check_id(q,q1,q2,s,b_year,b_month) :
    while q1.startswith('0' or '1' or '2'):
        y = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x')
        if y == 'o' and q2.startswith('1'or'2') :
            print('질못된 번호입니다.')
        elif y == 'o' and q2.startswith('3'or'4') :
            print(f'{b_year}년{b_month}월 {s}')
        else :
            print(f'{b_year}년{b_month}월 {s}')
            break
a = check_id(q,q1,q2,s,b_year,b_month)
print(a)



