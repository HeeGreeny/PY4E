from operator import eq


def grader():
    # 학생 답
    s = ["김갑,3242524215",
    "이을,3242524223",
    "박병,2242554131",
    "최정,4245242315",
    "정무,3242524315"]
    # 정답지
    a = [3,2,4,2,5,2,4,3,1,2]
    # 콤마를 기준으로 라인 슬라이스
    lin = [i.split(','[0]) for i in s]
    for i in range(len(lin)):
    # 답안은 2번째 인덱스
        score = lin[i][1]
    # 답안을 정답지에 맞춰 리스트화
        scores = list(map(int, score))
    # 답안과 정답지 비교해서 일치하는 수 합계
        compare = sum(map(eq, a, scores))
    # 일치수 합계를 라인 1번째 인덱스로 추가
        lin[i].insert(0, compare)
    # 라인 1번째 인덱스 내림차순 정렬
    lins = sorted(lin, reverse=True)
    # 라인 에서 이름, 점수, 등수 가져와서 출력
    for i in range(len(lins)):
        names = lins[i][1]
        compares = lins[i][0]
        print(f'학생: {names} 점수: {compares*10}점 {i+1}등')


grader()
