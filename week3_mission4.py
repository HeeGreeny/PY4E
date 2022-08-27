n = int(input('첫 번째 수 입력: '))
m = int(input('두 번째 수 입력: '))

def count_prime_number(n,m) :
    count = 0
    for i in range(n, m + 1):
        y = 0
        for x in range(1, i+1):
            if i % x == 0:
                y += 1
        if y == 2 :
            count +=1
    print('소수개수',count)

if __name__ == "__main__" :
    count_prime_number(n,m)