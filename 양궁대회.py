# 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
from collections import deque
def solution(n, info):
    def check(arr1,arr2):
        # arr1은 어피치, arr2는 라이언
        a1 = 0
        a2 = 0
        for i in range(11):
            if arr1[i] == 0 and arr2[i] ==0:
                continue
            elif arr1[i] >= arr2[i]:
                a1 += 10-i
            else:
                a2 += 10-i
        return a2-a1
    def compare(arr1,arr2):
        # arr1은 기존값, arr2는 새로운값
        for i in range(11)[::-1]:
            if arr1[i] > arr2[i]:
                return False
            elif arr1[i] < arr2[i]:
                return True
        return False

    answer = []
    max_value = 0
    que = deque()
    que.append((n,0,[]))
    while que:
        arrow,idx,arr = que.popleft()
        if arrow == 0:
            l = 11-len(arr)
            arr += [0]*l
            point_gap = check(info,arr)
            if max_value < point_gap:
                max_value = point_gap
                answer = arr
            elif max_value and max_value == point_gap and compare(answer,arr):
                answer = arr
            continue
        if idx == 10:
            que.append((0,idx+1,arr+[arrow]))
            continue
        use = info[idx]+1
        # 이번 점수는 가져가자
        if arrow-use >= 0:
            que.append((arrow-use,idx+1,arr+[use]))
        # 이번 점수는 포기
        que.append((arrow,idx+1,arr+[0]))
    if not answer:
        answer = [-1]
    return answer

ans = solution(1,[1,0,0,0,0,0,0,0,0,0,0])
print(ans)