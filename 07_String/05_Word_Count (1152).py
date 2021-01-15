# 영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다.
# 이 문자열이 몇 개의 단어로 이루어져 있는지 구하는 프로그램을 작성하라.
# 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
case = list(input().split())
count = 0

for i in range(len(case)):
    count += 1
print(count)