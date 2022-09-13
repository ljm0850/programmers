def solution(s):
    answer = ''
    numbers = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    temp = ''
    for alpha in s:
        if alpha.isdigit():
            answer += alpha
        else:
            temp += alpha
            if numbers.get(temp):
                answer += numbers[temp]
                temp = ''

    return int(answer)