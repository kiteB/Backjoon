# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지를 알아내는 프로그램을 작성하시오.
# 단, 대소문자를 구분하지 않는다.
# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
from collections import Counter

case = input().upper()
counter = Counter(case).most_common()

if len(case) == 1:
    print(case.upper())
else:
    if counter[0][1] == counter[1][1]:
        print('?')
    else:
        print(counter[0][0].upper())
