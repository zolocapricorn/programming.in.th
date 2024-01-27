def worldcup():
    country = [input() for _ in range(4)]
    score = [input().split(" ") for _ in range(4)]
    count = 0
    result = []
    for first in range(4):
        for second in range(4):
            if country[first] == country[second]:
                pass
            elif score[first][second] > score[second][first]:
                count += 3
            elif score[first][second] == score[second][first]:
                count += 1
        result.append(str(count))
        count = 0
    
    name, total = zip(*sorted(zip(result, country), reverse=True))
    for seq in range(4):
        print(name[seq] + " " + total[seq])
worldcup()

