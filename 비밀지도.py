def solution(n, arr1, arr2):
    answer = [""]*n
    for i in range(n):
        target1 = bin(arr1[i])[2:]
        target2 = bin(arr2[i])[2:]
        t1 = n-len(target1)
        t2 = n-len(target2)
        target1 = '0'*t1 + target1
        target2 = '0'*t2 + target2
        for idx in range(n):
            if target1[idx] == '1' or target2[idx] == '1':
                answer[i] += "#"
            else:
                answer[i] += " "
    return answer