def foo(ids):

    ids = list(set(ids))
    ids.sort()

    for i in range(len(ids)):
        if i != ids[i]:
            return i

    return len(ids)
