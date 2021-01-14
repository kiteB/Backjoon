# N개의 정수가 주어질 때, 최솟값과 최댓값을 구하여라.
N = int(input())

arr = list(map(int, input().split()))
print(min(arr), max(arr))