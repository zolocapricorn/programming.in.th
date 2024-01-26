def skocimis(location):
    a, b, c = int(location[0]), int(location[1]), int(location[2])
    if (c-b-1) >= (b-a-1):
        print(c-b-1)
    else:
        print(b-a-1)
skocimis(input().split(" "))

