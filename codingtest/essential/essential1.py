def foo(nums, target):

    hash_map = {}
    for index, num in enumerate(nums):
        result = target - num
        if result in hash_map:
            return [hash_map[result], index]
        hash_map[num] = index
    return
