def abc(number, alphabet):
    con_num = sorted([int(x) for x in number])
    keep = {"A": con_num[0], "B": con_num[1], "C": con_num[2]}
    for i in alphabet:
        if i == "A":
            print(keep.get(i), end = " ")
        elif i == "B":
            print(keep.get(i), end = " ")
        else:
            print(keep.get(i), end = " ")
abc(input().split(), input())

