from collections import deque

result = []

while True:
    text = input().rstrip()
    if text == ".":  # 종료 조건
        break

    stack = deque()
    is_balanced = True

    for char in text:
        if char in "([":  # 여는 괄호를 스택에 추가
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_balanced = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                is_balanced = False
                break

    if stack:  # 스택에 남아 있는 괄호가 있으면 균형이 맞지 않음
        is_balanced = False

    result.append("yes" if is_balanced else "no")

# 결과 출력
print("\n".join(result))
