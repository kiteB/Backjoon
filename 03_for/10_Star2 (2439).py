# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만 오른쪽으로 정렬하도록 출력하기
N = int(input())

for i in range(1, N+1):
    print('{0}{1}'.format(' '*(N-i), '*'*i))
    # print(' '*(N-i)+'*'*i)로 수정 가능!