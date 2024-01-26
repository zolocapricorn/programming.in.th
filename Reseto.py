def reseto(integer):
    number, killer = int(integer[0]), int(integer[1])
    result = []
    for start in range(2, number+1):
        for find in range(2, number+1):
            if find%start == 0 and find not in result:
                result.append(find)
    print(result[killer-1])
reseto(input().split(" "))

