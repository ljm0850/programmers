def solution(n, k):
    def check_prime_num(num:int)->bool:
        if num == 1:
            return False
        i = 2
        while i **2 <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    def find_num(target:int,mod:int)->dict:
        temp = ""
        nums = {}
        while target:
            t = target % mod
            if t == 0:
                if temp:
                    nums[int(temp)] = nums.get(int(temp),0) +1
                    temp = ""
            else:
                temp = str(t) + temp
            target //= mod
        if temp:
            nums[int(temp)] = nums.get(int(temp),0) +1
        return nums

    nums = find_num(n,k)
    print(nums)
    answer = 0

    for num in nums:
        if check_prime_num(num):
            answer += nums[num]
    return answer
ans = solution(437674,3)
print(ans)