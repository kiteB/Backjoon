# 두 정수 A, B를 입력받은 다음, A+B를 출력하는 프로그램 작성
T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print('Case #{0}: {1} + {2} = {3}'.format(i, a, b, a+b))