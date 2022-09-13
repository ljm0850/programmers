import heapq
def solution(n:int, s:int, a:int, b:int, fares:list)->int:
    road = [[] for _ in range(n+1)] # 그래프 기록, 1번지점에서 2번 지점 road[1][2] = value
    for far in fares:
        road[far[0]].append((far[1],far[2]))
        road[far[1]].append((far[0],far[2]))
    INF = 20000001 # n<=200, 거리가 최대 100,000 // INF는 나올수 없는 높은 값
    answer = INF
    # 최저 비용 기록, 2지점에서 3지점 최저 비용 = shortcut[2][3]
    shortcut = [[INF]*(n+1) for _ in range(n+1)] # short[1][2] = value
    # 시작위치에서 그대로 있을때는 0만큼 값이 드는것 기록(출발지점에서 바로 찢어지는게 유리할 경우 필요)
    for node in range(1,n+1):
        shortcut[node][node] = 0
    # 다익스트라
    def dijkstra(start:int)->None:
        heap = [(0,start)]
        while heap:
            now_pay,now = heapq.heappop(heap)
            # 반복문 도는 사이 더 싼 값이 나와서 해당 값이 필요없으면 계산을 포기
            if now_pay > shortcut[start][now]:continue
            for next,add_pay in road[now]:
                next_pay = now_pay + add_pay
                # 값갱신,기존 루트보다 저렴하면 나머지 경로 다시 계산
                if next_pay < shortcut[start][next]:
                    heapq.heappush(heap,(next_pay,next))
                    shortcut[start][next] = next_pay
    # 모든 지점에서 최저 비용 기록
    # for start in range(1,n+1):
    #     dijkstra(start)
    for start in (s,a,b):
        dijkstra(start)

    # 중간지점까지 같이 가고 각자 나눠 간다는 개념(시작점->중간지점 + 중간지점-> a지점 + 중간지점->b지점)
    for middle_node in range(1,n+1):
        # answer = min(answer,shortcut[s][middle_node]+shortcut[middle_node][a]+shortcut[middle_node][b])
        answer = min(answer,shortcut[s][middle_node]+shortcut[a][middle_node]+shortcut[b][middle_node])
    return answer