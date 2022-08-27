guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

def wrong_guest_book(my_list) :
    for n in range(len(my_list)) :
          if ('010' in my_list[n][1]) and ('-' in my_list[n][1]) and (len(my_list[n][1]) == 13) :
              pass
          else :
              print('잘못 쓴 사람:', my_list[n][0])
              print('잘못 쓴 번호', my_list[n][1],'\n')

def main() :
    to_list = list(guest_book.split('\n'))
    my_list = [i.split(','[0]) for i in to_list]
    with open('guest_book.txt', 'a', encoding='utf8') as f:
        f.write(guest_book)
    wrong_guest_book(my_list)

if __name__ == "__main__" :
    main()



