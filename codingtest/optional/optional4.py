def foo(numbers):
    number_list = list(map(int, numbers.split()))
    odd_list = []
    even_list = []
    for i in range(len(number_list)):
        if number_list[i] % 2 == 1:
            odd_list.append(i + 1)
        else:
            even_list.append(i + 1)
    if len(odd_list) == 1:
        return odd_list[0]
    if len(even_list) == 1:
        return even_list[0]
