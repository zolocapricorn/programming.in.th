def main(keep, mid, last):
    summ = keep + mid + last
    if summ >= 80:
        return "A"
    elif summ >= 75:
        return "B+"
    elif summ >= 70:
        return "B"
    elif summ >= 65:
        return "C+"
    elif summ >= 60:
        return "C"
    elif summ >= 55:
        return "D+"
    elif summ >= 50:
        return "D"
    return "F"
print(main(int(input()), int(input()), int(input())))

