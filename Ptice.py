def ptice(number, alphabet):
    Adrian = ["A", "B", "C"]
    Bruno = ["B", "A", "B", "C"]
    Goran = ["C", "C", "A", "A", "B", "B"]
    count_A, count_B, count_G = 0, 0, 0
    for a in range(len(alphabet)):
        if Adrian[a%3] == alphabet[a]:
            count_A += 1
        if Bruno[a%4] == alphabet[a]:
            count_B += 1
        if Goran[a%6] == alphabet[a]:
            count_G += 1
    if [count_A, count_B, count_G] == number:
        print(number)
    print(max(count_A, count_B, count_G))
    if count_A == max(count_A, count_B, count_G):
        print("Adrian")
    if count_B == max(count_A, count_B, count_G):
        print("Bruno")
    if count_G == max(count_A, count_B, count_G):
        print("Goran")
ptice(int(input()), input())

