# 문자가 아닌 이름 input 입력오류 체크
while True :
    name = input('이름을 입력하세요: ')
    if name.isalpha() is False:
       print('이름을 정확히 입력하세요!')
       exit()
    else :
       break
# 숫자가 아닌 점수 input 입력오류 체크
while True :
    score = input('점수를 입력하세요: ')
    try :
        score = int(score)
        break
    except ValueError :
       print('점수를 정확히 입력하세요!')
       exit()
#점수에 따른 학점 계산
def your_grade() :
    if 95 <= score <= 100 :
       grade = 'A+'
    elif 90 <= score <= 94 :
       grade = 'A'
    elif 85 <= score <= 89 :
       grade = 'B+'
    elif 80 <= score <= 84 :
       grade = 'B'
    elif 75 <= score <= 79 :
       grade = 'C+'
    elif 70 <= score <= 74 :
       grade = 'C'
    elif 65 <= score <= 69 :
       grade = 'D+'
    elif 60 <= score <= 64 :
       grade = 'D'
    elif score < 60 :
       grade = 'F'
    else :
        print('다시 입력해주세요.')
    return grade
# 이름,점수,학점 출력
grader = your_grade()
print('학생이름:',name)
print(f'점수: {score}점')
print('학점:',grader)
