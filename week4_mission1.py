# Easy version
# m = int(input("천단위 이상의 숫자를 넣어주세요: "))
# def make_comma(m) :
#     if not m >= 1000 :
#        print("계산가능한 천단위 이상의 숫자를 넣어주세요")
#     else :
#         print(f"{m:,}")


def make_comma(m):
        s = '%d' % m
        groups = []
        while s and s[-1].isdigit():
            groups.append(s[-3:])
            s = s[:-3]
        print(s + ','.join(reversed(groups)))

def main() :
    while True :
        try :
            m = int(input("숫자를 넣어주세요: "))
            if not m >= 1000:
                print("계산가능한 천단위 이상의 숫자를 넣어주세요\n")
            else:
               break
        except :
            print("숫자만 입력해주세요!!\n")
    make_comma(m)

if __name__ == "__main__" :
    main()

