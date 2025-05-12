def foo(s):
    result_list = []
    for i in s:

        if i == "(" or i == "[" or i == "{":
            result_list.append(i)
        else:
            if len(result_list) == 0:
                return False
            elif i == ")":
                if result_list.pop() != "(":
                    return False
            elif i == "]":
                if result_list.pop() != "[":

                    return False
            elif i == "}":
                if result_list.pop() != "{":
                    return False
    if len(result_list) == 0:
        return True
    return False
