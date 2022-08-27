import statistics

n = int(input('첫 번째 수 입력: '))
m = int(input('두 번째 수 입력: '))

def find_even_number(n,m) :
    numbers = [i for i in range(n, m + 1)]
    mid = statistics.median(numbers)
    for e in numbers :
        if e%2 == 0 :
            print(e,'짝수')
            if e == mid :
                print(mid,"중앙값")

if __name__ == "__main__" :
    find_even_number(n,m)


# x = len(numbers)
#     if x % 2 == 1:
#        m = numbers[int((x-1)/2)]
#        print(m,'중앙값')