# 각 테스트 케이스마다 A+B를 한 줄에 하나씩 순서대로 출력하기
# input 대신 sys.stdin.readline을 사용하기
import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
