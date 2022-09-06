def solution(id_list:list, report:list, k:int)-> list:
    check = {}  # 신고 누적용,
    email_cnt = {}  # 이메일 몇개 받는지 기록
    answer = [] # 정답
    for id in id_list:
        # 한 유저가 같은 유저 여러번 신고한 경우 신고 횟수 1회 처리를 위해 set
        check[id] = set()
        email_cnt[id] = 0
    # 신고 기록
    for rep in report:
        user,target = rep.split()
        check[target].add(user)
    # 신고 기록에 따라 이메일 개수 추가
    for id in id_list:
        cnt = len(check[id])
        if cnt >= k:
            # 해당 유저를 신고한 사람이 check[id]에 들어가 있음
            for id in check[id]:
                email_cnt[id] += 1
    # id_list 순서대로 값을 메일 개수 기록
    for id in id_list:
        answer.append(email_cnt[id])
    return answer
