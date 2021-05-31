def main(dm):
    day = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
    month = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    change = [int(a) for a in dm]
    print(day[(change[0]+(month[change[1]-1]))%7])
main(input().split())