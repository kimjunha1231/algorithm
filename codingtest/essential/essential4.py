def foo(str):
    count = 0
    result = ""
    line = ""
    for char in str:
        if ord(char) > 122:
            count += 2
        else:
            count += 1
        if count >= 80:
            result += line + "\n"
            line = ""
            count = 0
        line += char
    if line:
        result += line
    return result
