def main(A, opr, B):
    if opr == "*":
        point = (A.count("0"))+(B.count("0"))
        print(1, end="")
        for a in range(point):
            print(0, end="")
    else:
        if len(A) < len(B):
            B = A
        keep = [ b for b in A]
        for c in range(len(B)):
            keep.pop(-1)
        for d in B:
            keep.append(d)
        print(*keep, sep="")
        else:
            
main(input(), input(), input())