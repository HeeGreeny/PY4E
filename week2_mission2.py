monthly_payment = input('월급을 숫자로 입력하세요(___만원): ')
# 숫자가 아닌 input 입력오류 체크
try :
    annual_payment = 12 * int(monthly_payment)
except :
    print('숫자만 입력하세요!')
    quit()
# 연봉에 따른 세율 계산
def annual_tax () :
    if annual_payment <= 1200 :
       aftertax = annual_payment - (annual_payment * 0.06)
    elif 1200 < annual_payment <= 4600 :
       aftertax = annual_payment - (annual_payment * 0.15)
    elif 4600 < annual_payment <= 8800 :
       aftertax = annual_payment - (annual_payment * 0.24)
    elif 8800 < annual_payment <= 15000 :
       aftertax = annual_payment - (annual_payment * 0.35)
    elif 15000 < annual_payment <= 30000 :
       aftertax = annual_payment - (annual_payment * 0.38)
    elif 30000 < annual_payment <= 50000 :
       aftertax = annual_payment - (annual_payment * 0.40)
    elif 50000 < annual_payment :
       aftertax = annual_payment - (annual_payment * 0.42)
    else :
        print('다시 입력해주세요.')
    return aftertax
# 세전, 세후 연봉 출력
aftertax_payment = annual_tax()
print(f'세전 연봉: {annual_payment}만원')
print(f'세후 연봉: {int(aftertax_payment)}만원')