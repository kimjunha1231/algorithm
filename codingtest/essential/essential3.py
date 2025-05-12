def foo(games):
    score = 0
    for game in games:

        left, right = map(int, game.split(":"))
        if left > right:
            score += 3
        elif left == right:
            score += 1
    return score
