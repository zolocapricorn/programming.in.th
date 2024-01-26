from itertools import combinations as cbnt
def perket(igd):
    result = []
    data = [[int(b) for b in input().split()] for a in range(igd)]
    for c in range(1, igd+1):
        if c == 1:
            result += [abs(d[0]-d[1]) for d in data]
        else:
            think = list(cbnt(data, c))
            for e in think:
                sour, bt = 1, 0
                for f in range(len(e)):
                    sour *= e[f][0]
                    bt += e[f][1]
                result.append(abs(sour-bt))
    print(min(result))
perket(int(input()))

