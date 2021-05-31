def main(number):
    change = sorted([int(a) for a in number])
    print(change[0]*change[2])
main(input().strip().split())