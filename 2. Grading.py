def main(keep, mid, last):
    summ = keep + mid + last
    if summ >= 80:
        print("A")
    elif summ >= 75:
        print("B+")
    elif summ >= 70:
        print("B")
    elif summ >= 65:
        print("C+")
    elif summ >= 60:
        print("C")
    elif summ >= 55:
        print("D+")
    elif summ >= 50:
        print("D")
    else:
        print("F")

main(int(input()), int(input()), int(input()))