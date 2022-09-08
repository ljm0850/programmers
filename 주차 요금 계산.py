def solution(fees, records):
    # fee = [기본시간,기본요금,단위시간,단위요금]
    # records = ["시각 차량번호 in(out)"]
    check = {} # {car_number:["05:10"] }
    answer = []
    for record in records:
        time, car_number, event = record.split()
        check[car_number] = check.get(car_number, []) + [time]

    for car_number,times in check.items():
        max_idx = len(times) - 1
        total_time = 0
        # 주차장에 있었던 시간 계산
        for idx in range(0, len(times), 2):
            intime = int(times[idx][:2]) * 60 + int(times[idx][3:5])
            if idx == max_idx: # 나간적이 없다
                outtime = 1439
            else:
                outtime = int(times[idx + 1][:2]) * 60 + int(times[idx + 1][3:5])
            total_time += outtime - intime

        over_time = total_time - fees[0]
        pay = fees[1]

        if over_time > 0:
            pay += over_time // fees[2] * fees[3]
            if over_time % fees[2]: pay += fees[3]
        answer.append((int(car_number),pay))
    answer.sort(key=lambda x:x[0])
    return_value = []
    for ans in answer:
        return_value.append(ans[1])
    return return_value