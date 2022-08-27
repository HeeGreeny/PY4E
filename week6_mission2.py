def sales_management(member_names, member_records):
    dict_list = dict(zip(member_names, member_records))  # 딕셔너리에 이름,실적 저장
    aver_di = {}  # 평균값 넣을 딕셔너리 생성
    for k, v in dict_list.items():  # 평균 실적 계산
        aver_di[k] = sum(v)/len(v)
    s_list = sorted([[v, k] for k, v in aver_di.items()], reverse=True)  # value값 기준으로 내림차순
    b_list = list(s_list[:2])  # 보너스 대상자 1,2등 / 면담 대상자 5,6등 추출
    l_list = list(s_list[4:])
    for i in b_list:  # 각 조건 해당하면 출력
        if i[0] > 5:
            print('보너스 대상자', i[1])
    for i in l_list:
        if i[0] < 3:
            print('면담 대상자', i[1])


def main():
    # 이름, 실적
    member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
    member_records = [[4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5], [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
                      [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1], [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
                      [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9], [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3]]

    sales_management(member_names, member_records)


if __name__ == "__main__":
    main()


    # # 보너스 대상자 선정 조건
    # if (s_list[0][0]) > 5:
    #     print('보너스 대상자',s_list[0][1])
    # if (s_list[1][0]) > 5:
    #     print('보너스 대상자',s_list[1][1])
    # # 면담 대상자 선정 조건
    # if (s_list[4][0]) < 3:
    #     print('면담 대상자', s_list[4][1])
    # if (s_list[5][0]) < 3:
    #     print('면담 대상자', s_list[5][1])
