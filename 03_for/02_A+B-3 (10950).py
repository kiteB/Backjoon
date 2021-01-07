# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램 작성
# 첫 줄에는 테스트 케이스의 개수 T가 주어짐.
T = int(input())

for i in range(T):
    a, b = map(int, input().split())

    print(a+b)
