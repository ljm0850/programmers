from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    if not cacheSize:
        return len(cities)*5
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        elif len(cache) < cacheSize:
            cache.append(city)
            answer += 5
        else:
            cache.popleft()
            cache.append(city)
            answer += 5
    return answer

ans=solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
print(ans)