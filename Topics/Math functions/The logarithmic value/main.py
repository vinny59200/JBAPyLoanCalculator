import math

first = int(input())
second = int(input())
if second < 0 or second == 0 or second == 1:
    log = round(math.log(first),2)
    print(log)
else:
    log = round(math.log(first, second),2)
    print(log)
