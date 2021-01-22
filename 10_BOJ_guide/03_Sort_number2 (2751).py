# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
from sys import stdin

N = int(stdin.readline())
numbers = []

for i in range(N):
    numbers.append(int(stdin.readline()))
numbers.sort()

for i in numbers:
    print(i)