def foo(s):
    numberResult = 0
    number_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev_num = 0

    for i in reversed(s):

        now_number = number_dic[i]
        if now_number < prev_num:
            numberResult -= now_number
        else:
            numberResult += now_number
        prev_num = now_number

    return numberResult


print(foo("IV"))
print(foo("LVIII"))
print(foo("MCMXCIV"))
print(foo("MCMXL"))
print(foo("CCXXXV"))
print(foo("DLIII"))
print(foo("MMCDXCIII"))
