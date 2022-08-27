def king(korea_king, chosun_king):
    tmp_k = korea_king.split(',')  # 왕이름 슬라이스
    tmp_c = chosun_king.split(',')
    k_king = set(tmp_k)   # set으로 묶어줌
    c_king = set(tmp_c)
    result = set(k_king) & set(c_king)  # 교집합 찾기
    c = len(result)  # 교집합 수
    for k in result:  # 교집합 해당 이름 하나씩 출력 + 교집합 수 출력
        print('조선과 고려에 모두 있는 왕 이름 :', k)
    print(f'조선과 고려에 모두 있는 왕 이름은 총 {c}개 입니다')


def main():
    # 왕이름
    korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
    chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"

    king(korea_king, chosun_king)


if __name__ == "__main__":
    main()


    # for w in k_king:
    #     tmp_k[w] = tmp_k.get(w)
    # for w in c_king:
    #     tmp_c[w] = tmp_c.get(w)
    # print(tmp_k)
    # print(type(tmp_k))
    # k_list = []
    # c = 0
    # for k in k_king :
    #     if k in c_king :
    #         k_list.append(k)
    #         if k in k_list :
    #             pass
    #             c = c+1
    #             print('조선과 고려에 모두 있는 왕 이름 :',k)
    #
    # print(k_king)
    #
    # a =tmp_k.intersection(tmp_c)
    # print(a)
