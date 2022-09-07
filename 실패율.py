def solution(N, stages):
    ratio = {}  # {stage:[머물고 있는 사람 수,전체 도달사람수]}
    # 세팅
    for stage in range(1, N + 2):
        ratio[stage] = [0, 0]
    # 스테이지 기록
    for stay_stage in stages:
        ratio[stay_stage][0] += 1
        for stage in range(1, stay_stage + 1):  # 이 부분이 비 효율적, 한번에 + 시키는게 효율적
            ratio[stage][1] += 1

    temp = []  # [(실패율,stage)]
    for key, value in ratio.items():
        if value[1]:
            temp.append((value[0] / value[1], key))
        else:
            temp.append((0, key))
    # 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
    temp.sort(key=lambda x: x[1])
    # 실패율 높은 순서 내림차순
    temp.sort(key=lambda x: -x[0])
    temp.sort(key=lambda x: [-x[0],x[1]])

    # stage만 뺴오기
    answer = []
    for stage in temp:
        if stage[1] != N + 1:
            answer.append(stage[1])
    return answer