# 첫째 줄에 N(정수 개수)과 정수 X가 주어지고, 둘쨰 줄에 수열 A를 이루는 정수 N개가 주어진다.
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력하기
N, X = map(int, input().split())
n = list(map(int, input().split()))

for i in range(N):
    if n[i] < X:
        print(n[i], end=' ')