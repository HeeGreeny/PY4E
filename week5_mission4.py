from datetime import datetime, timedelta


def after_100():
    try:
        week = ['월','화','수','목','금','토','일']
        dates = input("그/그녀와 사귀게 된 날짜를 입력해주세요 (ex.20220815): ")
        year = int(dates[:4])
        month = int(dates[4:6])
        day = int(dates[6:])
        ourday = datetime.strptime(dates, "%Y%m%d")
        theday = ourday+timedelta(days=99)
        y = theday.year
        m = theday.month
        d = theday.day
        weekday = week[datetime(year, month, day).weekday()]
        theweekday = week[theday.weekday()]
        print(f'{year}년 {month}월 {day}일 {weekday}요일부터 100일 뒤는 {y}년 {m}월 {d}일 {theweekday}요일')
    except ValueError:
        print('정확한 날짜를 숫자로 입력해주세요!')
        exit()


print('...저...우리...오늘부터..1일 어때.....?')
# # 결과 출력
after_100()
