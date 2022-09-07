# 아이디는 3글자 이상 15자 이하
# 알파벳 소문자, -, _, . 만 사용
# .은 처음과 끝에 사용 불가, 연속 사용 불가
def solution(new_id):
    # 1단계
    step1 = new_id.lower()
    # 2단계
    step2 = ''
    for alpha in step1:
        if alpha.isalpha() or alpha.isdigit() or alpha in ('-', '_', '.'):
            step2 += alpha
    # 3단계
    while True:
        temp = step2.replace('..', '.')
        if temp == step2:
            break
        else:
            step2 = temp
    step3 = temp
    # 4단계
    while True:
        if not step3:
            step4 = ""
            break
        elif step3[0] == '.':
            step3 = step3[1:]
        elif step3[-1] == '.':
            step3 = step3[:len(step3)-1]
        else:
            step4 = step3
            break
    # 5단계
    if not step4: step5 = "a"
    else: step5 = step4
    # 6단계
    if len(step5) >= 16:
        step6 = step5[:15]
        if step6[-1] == '.':
            step6 = step6[:14]
    else: step6 = step5
    # 7단계
    step7 = step6
    while len(step7) <=2:
        step7 += step7[-1]
    return step7

solution("abcdefghijklmn.p")
import re
new_string = re.sub('[0-9]+', '', '0 8 l 5 j m 0')
# new_string = 'ljm'
print(new_string)