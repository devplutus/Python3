import math
r = int(input())
# 유클리드 기하학
# pi * R * R
print(round(math.pi * (r**2), 6))
# 택시 기하학
# 2 * R * R
print("%0.6f" % (2 * (r**2)))