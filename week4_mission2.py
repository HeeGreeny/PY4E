a = """선운사에서 / 최영미
꽃이 피는 건 힘들어도 지는 건 잠깐이더군
골고루 쳐다볼 틈 없이 님 한 번 생각할 틈 없이 아주 잠깐이더군
그대가 처음 내 속에 피어날 때처럼 잊는 것 또한 그렇게 순간이면 좋겠네
멀리서 웃는 그대여 산 넘어 가는 그대여 꽃이 지는 건 쉬워도 잊는 건 한참이더군 영영 한참이더군"""

def count_word() :
    print(a)
    while True :
        try :
            q = input("\n카운트를 원하는 단어를 넣어주세요: ")
            if q not in a:
                print("찾을 수 없는 단어입니다.")
            else:
                print(a.count(q),'개의',q,'이 있습니다.')
                with open('You.txt', 'w', encoding = 'UTF-8') as f:
                    f.write(a)
                    print('txt 파일 저장완료')
                break
        except:
            print("단어를 입력해주세요!\n")

count_word()

#
# def main() :
#     while True :
#         try :
#             print(a)
#             q = input("\n카운트를 원하는 단어를 넣어주세요: ")
#             if q not in a :
#                 print("찾을 수 없는 단어입니다.\n")
#             else:
#                break
#         except :
#             print("단어를 입력해주세요!\\n")
#     count_word()
#
# if __name__ == "__main__" :
#     main()

