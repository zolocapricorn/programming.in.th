import math
def herman(radius):
    general = math.pi*(radius**2)
    area = 2*(radius**2)
    print("%.6f\n%.6f" % (general, area))
herman(int(input()))

