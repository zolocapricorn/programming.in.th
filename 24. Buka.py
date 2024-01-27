def buka(first, operand, second):
    if operand == "+":
        print(first+second)
    else:
        print(first*second)
            
buka(int(input()), input(), int(input()))

