# 노트북 가격이 C만원으로 책정되었다고 가정한다.
# 일반적으로 생산 대수를 늘리면 어느 순간 총 수입이 총 비용보다 많아지게 된다.
# 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점이라고 한다.
# A (고정 바용), B (가변 비용), C (노트북 가격)가 주어졌을 때, 손익분기점을 구하시오.
A, B, C = map(int, input().split())

if C <= B:
    print(-1)
else:
    print(int(A/(C-B)+1))
