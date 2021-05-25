def main(num, alphabet):
    con_num = [int(x) for x in num]
    s_num = sorted(con_num)
    keep = {"A": s_num[0], "B": s_num[1], "C": s_num[2]}
    for i in alphabet:
        if i == "A":
            print(keep["A"], end = " ")
        elif i == "B":
            print(keep["B"], end = " ")
        else:
            print(keep["C"], end = " ")
main(input().split(), input())