import sys


def solve():
    # 입력을 한 번에 읽고, 공백을 기준으로 나눔
    data = sys.stdin.read().split()

    # 첫 번째 값은 N이므로 제외하고 숫자 처리
    numbers = [int(num[::-1]) for num in data[1:]]  # 숫자 문자열을 뒤집고 정수 변환

    # 정렬
    numbers.sort()

    # 출력
    print("\n".join(map(str, numbers)))  # 개행으로 출력


solve()
