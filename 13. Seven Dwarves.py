def main():
    lists = []
    for a in range(9):
        lists.append(int(input()))
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
main()