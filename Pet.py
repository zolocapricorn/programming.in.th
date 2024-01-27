def pet():
    ans = []
    result = [sum([int(b) for b in input().split()]) for a in range(5)]
    ans.append(result.index(max(result))+1)
    ans.append(max(result))
    print(*ans)
pet()

