def main(data, mt1, mt2, result):
    rc = [int(a) for a in data]
    for b in range(rc[0]):
        mt1.append([int(c) for c in input().split()])
    for d in range(rc[0]):
        mt2.append([int(e) for e in input().split()])
    for f in range(rc[0]):
        for g in range(rc[1]):
            result.append(mt1[f][g]+mt2[f][g])
            if g == rc[1]-1:
                print(*result)
                result = []
main(input().split(), [], [], [])