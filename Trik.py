def trik(alphabet):
    ball = [1, 2, 3]
    for i in alphabet:
        if i == "A":
            point = ball[1]
            ball[1] = ball[0]
            ball[0] = point
        elif i == "B":
            point = ball[2]
            ball[2] = ball[1]
            ball[1] = point
        else:
            point = ball[2]
            ball[2] = ball[0]
            ball[0] = point
    for position in range(len(ball)):
        if ball[position] == 1:
            print(position + 1)
trik(input())

