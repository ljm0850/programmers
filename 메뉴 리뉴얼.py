from itertools import combinations


def solution(orders: list, course: list) -> list:
    cnt = [{} for _ in range(len(course))]  # 단품메뉴 개수로 나눠서 들어감 [{('A','B'):3,...}, {}, ...]
    answer = []
    for order in orders:
        for i in range(len(course)):
            l = course[i]
            # 부분집합을 combinations으로 구함,
            # "WXA"를 정렬하여 "AWX"로 바꾼 후 부분집합 구하기 위해 sorted(order)
            target = combinations(sorted(order), l)
            for t in target:
                # 값이 있으면 기존값+1, 없으면 0+1
                cnt[i][t] = cnt[i].get(t, 0) + 1
    # target = {('X', 'Y'): 2, ('X', 'Z'): 1,...}
    for target in cnt:
        max_value = 2
        temp = []  # 가장 많이 주문한 메뉴가 temp에 들어가게 설계
        for key, value in target.items():
            # 최고값 갱신되면 temp값 변경, max_value 변경
            if value > max_value:
                max_value = value
                temp = [key]
            # 최고값과 같으면 temp에 추가
            elif value == max_value:
                temp.append(key)

        for t in temp:
            if t: answer.append("".join(t))
    answer.sort()
    return answer