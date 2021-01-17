# 육각형으로 이루어진 벌집이 있을 때, 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다.
# 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지 (시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오.
N = int(input())
count = 1       # 필요한 방 개수 카운트
max_num = 1     # 방에서 가장 큰 값을 저장
if N == 1:
    print(1)
else:
    while True:
        if N <= max_num:    # N이 max_num (방에서 가장 큰 값) 보다 작거나 같으면
            print(count)    # count 그대로 출력
            break
        else:   # N이 max_num 보다 크면
            max_num += (6*count)    # max_num을 6*count 값만큼 증가시켜주기
            count += 1      # count도 증가
