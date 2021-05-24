import math
def main(radius):
    general = math.pi*(radius**2)
    area = 2*(radius**2)
    print("%.6f" % general)
    print("%.6f" % area)
main(int(input()))