def good_customer(info):
    a = info.split(',')
    for i in range(0,len(a), 6) :
        s_list = a[i:i+6]
        for i in s_list :
            id_list = []
            id = id_list.append(s_list[0])
        print(id)

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

def main():
    # 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
    info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

    good_customer(info)


if __name__ == "__main__":
    main()