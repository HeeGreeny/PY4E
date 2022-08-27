def good_customer(info):
    # 콤마를 기준으로 슬라이스 / 각 항목별 빈 리스트 생성
    a = info.split(',')
    ids, age, phone, sex, region, count = [], [], [], [], [], []
    # 6자릿마다 슬라이스 / 각 항목별로 리스트화
    for i in range(0, len(a), 6):
        lists = a[i:i+6]
        ids.append(lists[0])
        age.append(lists[1])
        phone.append(lists[2])
        sex.append(lists[3])
        region.append(lists[4])
        count.append(lists[5])
    # 전화번호가 없을시 000-0000-0000으로 변경
    phone = [w.replace('x', '000-0000-0000') for w in phone]
    # 구매횟수 int타입으로 변환
    count = list(map(int, count))
    # 회원정보 출력
    a_list = {'아이디': ids, '나이': age, '전화번호': phone, '성별': sex, '지역': region, '구매횟수': count}
    print(a_list)
    # 조건에 해당하는 할인쿠폰 대상자 출력
    b_list = {'아이디': lists[0], '나이': lists[1], '전화번호': lists[2], '성별': lists[3], '지역': lists[4], '구매횟수': lists[5]}
    if int(b_list['구매횟수']) > 8:
        if not b_list['전화번호'].isalpha():
            b_list = ','.join(f'{k}:{v}' for k, v in b_list.items())
            print('할인 쿠폰을 받을 회원정보', b_list)


def main():
    # 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
    info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

    good_customer(info)


if __name__ == "__main__":
    main()


        # for n in range(len(lists)) :
        #    id = lists[0]
        #    age = lists[1]
        #    phone = lists[2]
        #    sex = lists[3]
        #    region = lists[4]
        #    count = lists[5]
        #    di = {}
        #    di['아이디'] = id
        # print(di)


        # keys = ['아이디', '나이', '전화번호', '성별', '지역', '구매횟수']
        # values = [lists[0], lists[1], lists[2], lists[3], lists[4], lists[5]]

        #
        # for n in lists :
        #     d_list = {'아이디': lists[0],'나이': lists[1],'전화번호':lists[2],'성별':lists[3],'지역': lists[4],'구매횟수': lists[5]}
        #
        # print(d_list)
        # if int(d_list['구매횟수']) > 8 :
        #     if not d_list['전화번호'].isalpha() :
        #         print('할인 쿠폰을 받을 회원정보',d_list)




        # for keys, values in zip(keys,values):
        #    di[keys] = values
        # di['아이디'] = d_list['아이디']
        # di['나이'] = d_list['나이']
        # di['전화번호'] = d_list['전화번호']
        # di['성별'] = d_list['성별']
        # di['지역'] = d_list['지역']
        # di['구매횟수'] = d_list['구매횟수']
        # id = d_list['아이디']
        # age = d_list['나이']
        # phone = d_list['전화번호']
        # sex = d_list['성별']
        # region = d_list['지역']
        # count = d_list['구매횟수']

    # cst_list = {}

