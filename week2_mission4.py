# 숫자가 아닌 나이 input 입력오류 체크
while True :
    age = input('나이를 입력하세요: ')
    try:
        age = int(age)
        break
    except ValueError:
        print('나이를 숫자로 입력하세요!')
        exit()
# 문자가 아닌 지불유형 input 입력오류 체크
while True :
    how2pay = input('현금? 카드?: ')
    if how2pay.isalpha() is False:
        print("'현금' 혹은 '카드'를 입력하세요!")
        exit()
    else:
        break
#버스요금 계산
def bus_fare() :
    if (age < 8 or 75 <= age) and (how2pay == '카드' or how2pay =='현금'):
       fare = '무료'
    elif 8 <= age < 14 and (how2pay == '카드' or how2pay =='현금'):
       fare = '450원'
    elif 14 <= age < 20 and how2pay == '카드' :
       fare = '720원'
    elif 14 <= age < 20 and how2pay == '현금':
       fare = '1000원'
    elif 20 <= age and how2pay == '카드':
       fare = '1200원'
    elif 20 <= age and how2pay == '현금':
       fare = '1300원'
    else :
        pass
    return fare
# 나이,지불유형, 버스요금  출력
fares = bus_fare()
print(f'나이: {age}세')
print('지불유형:', how2pay)
print('버스요금:', fares)