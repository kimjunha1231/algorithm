import sys


def min_expression(expression: str) -> int:
    parts = expression.split("-")  # '-'를 기준으로 분리
    total = sum(map(int, parts[0].split("+")))  # 첫 번째 그룹은 더함

    for part in parts[1:]:  # 이후 그룹들은 전부 빼기 적용
        total -= sum(map(int, part.split("+")))

    return total


# 입력 처리
expression = input().strip()
print(min_expression(expression))
