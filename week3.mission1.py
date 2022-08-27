print('\n구구단을 외자! ¯\_(ツ)_/¯ 구구단을 외자! \n')
number = input("몇 단? : ")

def gugudan(number) :
    try :
        number = int(number)
        if number > 9 or number < 1:
            print('1과 9 사이의 숫자를 넣어주세요')
            quit()
        elif 1 <= number <= 9:
            print(number, '단')
            pass
        for i in range(1,10) :
           if i%2!=0 and number*i <= 50 :
               print(number, 'x', i, '=', number * i)
               continue
    except ValueError:
         print('숫자를 입력하세요!')
         exit()

if __name__ == "__main__" :
    gugudan(number)

