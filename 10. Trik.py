def main(alphabet):
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
    for i in range(len(ball)):
        if ball[i] == 1:
            print(i + 1)
main(input())