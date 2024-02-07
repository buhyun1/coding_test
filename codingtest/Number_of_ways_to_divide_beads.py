def solution(balls, share):
    # for 문 돌면서 모든 요소 곱하기
    ball_list = 1
    for i in range(1,balls+1):
        ball_list *= i
    
    share_list=1
    for j in range(1,balls-share+1):
        share_list *= j

    shared_list=1
    for k in range(1,share+1):
        shared_list *= k

    ans = ball_list//(share_list*shared_list)
    return ans

print(solution(5,3))
from itertools import permutations
# 순열과 조합을 쉽게 나타내주는 모듈이 있다.