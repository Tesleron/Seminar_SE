# author: itzhik aviv

import math
import sys

def main():
    sys.stdout = open("YPreults.txt", "w")
    print ("yosephus plavious problem:")
    k = 42
    for n in range(1, k):
      yp(n)
    sys.stdout.close()
def yp(n):
    l = [i for i in range(1, n + 1)]
    i = 0
    while (len(l) > 1):
        i = (i + 1) % len(l)
        l.remove(l[i])
    print("n = ", n, "survive by algorithm =", l[0],\
          "survive by formula =", \
          int(2 * (n - math.pow(\
              2, math.floor(math.log(n, 2)))) + 1))

main()
#shmokim meofefim123123
#or added this and this
x = 3