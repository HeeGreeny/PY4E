def stock_profit(stocks, sells):
    # 종목별로 나누기 / 매수종목, 매수평균금액 넣을 리스트 생성
    st_name = stocks.split(',')
    s_name = list()
    s_avg = list()
    # 종목안에서 항목별로 나누기 / 매수종목, 매수평균금액 리스트화
    for i in st_name:
        tmp_list = i.split('/')
        s_name.append(tmp_list[0])
        s_avg.append(tmp_list[2])
    # 매수평균금액 str -> int로 변환
    tmp_avg = list(map(int, s_avg))
    # 종목별 수익률 계산
    profit = [(sells[i] - tmp_avg[i]) / tmp_avg[i] * 100 for i in range(len(sells))]
    # 매수종목과 수익률 묶어서 리스트화
    s_profit = [[0 for _ in range(2)] for _ in range(len(s_name))]
    for i in range(len(s_name)):
        s_profit[i][0] = s_name[i]
        s_profit[i][1] = profit[i]
    # 수익률 기준으로 내림차순 정렬
    s_profit.sort(key=lambda x: -x[1])
    # 매수종목과 수익률 소수 둘째자리까지 반올림 출력
    for i in range(len(s_profit)):
        print(f"{s_profit[i][0]}의 수익률 {s_profit[i][1]:.2f}")


def main():
    # 매수종목, 수량, 매수평균금액
    stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
    # 판매가
    sells = [82000, 160000, 835000, 410000]

    stock_profit(stocks, sells)


if __name__ == "__main__":
    main()


#
# import math
# a = 2.66666666666
# b = math.floor(a*100)/100
# print(b)
# c = a*100//1/100
# print(c)
# d = int(a*100)/100
# print(d)
# e = math.floor(a)
# print(e)
# f = math.floor(a*100)//100
# print(f)
# print(f"{a:.3}")
# print(f"{a:.2f}")

# 수익률(%) = (판매가 - 매수평균금액) / 매수평균금액 * 100
