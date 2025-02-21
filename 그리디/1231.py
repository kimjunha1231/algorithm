import sys

# 입력 받기
n_list = list(sys.stdin.readline().strip())
n_list.sort()  # 사전순 정렬

# 문자 개수 카운트 딕셔너리
dic = {}
for i in n_list:
    dic[i] = dic.get(i, 0) + 1  # get()을 사용하여 깔끔하게 처리

# 팰린드롬을 만들기 위한 변수
middle = ""
left = []
odd_count = 0  # 홀수 개수 문자의 개수를 체크

# 정렬된 문자 순서로 반복
for key, value in sorted(dic.items()):  # 사전순 정렬
    if value % 2 == 1:
        odd_count += 1
        middle = key
        if odd_count > 1:  # 홀수 개수 문자가 2개 이상이면 팰린드롬 불가능
            print("I'm Sorry Hansoo")
            sys.exit()

    left.append(key * (value // 2))  # 절반을 left에 저장

right = left[::-1]  # left의 역순을 right로 설정

# 정답 출력
print("".join(left) + middle + "".join(right))
