# 두 자연수 A, B가 있을 때, A&B는 A를 B로 나눈 나머지이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한 뒤, 서로 다른 값이 몇 개 있는지 출력하기
numbers = []
remaining = []
count = []
result = 0

for i in range(10):
    numbers.append(int(input()) % 42)

numbers = set(numbers)
print(len(numbers))