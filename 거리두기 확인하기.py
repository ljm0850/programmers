def solution(places):
    dr,dc = (1,-1,0,0),(0,0,1,-1) # 상하좌우
    Dr,Dc = (1,1,-1,-1),(1,-1,1,-1) # 대각선
    answer = []
    
    def check(arr):
        for r in range(5):
            for c in range(5):
                if arr[r][c] == 'P':
                    for way in range(4):
						# 상하좌우 체크
                        nr,nc = r+dr[way],c+dc[way]
                        if 0<=nr<5 and 0<=nc<5 and arr[nr][nc] == 'P':
                            return 0
                        # 2칸 상하좌우 체크
                        nnr,nnc = r+2*dr[way], c+2*dc[way]
                        if 0<=nnr<5 and 0<=nnc<5 and arr[nnr][nnc] =='P' and arr[nr][nc] !='X':
                            return 0
                        # 대각선 체크
                        nr,nc = r+Dr[way],c+Dc[way]
                        if 0<=nr<5 and 0<=nc<5 and arr[nr][nc] == 'P' and not (arr[r][nc] == 'X' and arr[nr][c] == 'X'):
                            return 0
        return 1
                        
    for place in places:
        answer.append(check(place))
    
    return answer