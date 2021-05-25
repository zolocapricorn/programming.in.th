def main():
    result = []
    for i in range(10):
        number = int(input())
        result.append(number%42)
    keep = len(set(result))
    print(keep)
main()