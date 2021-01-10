# H와 M이 주어질 때, 45분을 뺐을 때의 시간 출력하기
hr, min = map(int, input().split())

if min > 44:
    print(hr, min-45)
elif min <= 44 and hr >= 1:
    print(hr-1, min+15)
else:
    print(23, min+15)