def main(result, ans):
    for a in range(5):
        data = sum([int(b) for b in input().split()])
        result.append(data)
    ans.append(result.index(max(result))+1)
    ans.append(max(result))
    print(*ans)
main([], [])