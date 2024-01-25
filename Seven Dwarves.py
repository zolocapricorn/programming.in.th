def seven_dwarves():
    lists = [int(input()) for _ in range(9)]
    cal = sum(lists)-100
    for b in lists:
        for c in lists:
            if b+c == cal:
                first = b
                second = c
    lists.remove(first)
    lists.remove(second)
    for d in lists:
        print(d)
seven_dwarves()

