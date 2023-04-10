# author: itzhik aviv

import math
import sys

def main():
    # sys.stdout = open("YPresultsGp.txt", "w")
    print("yosepush plaviuos genreal problem\n")
    yp(21, 1, 1)
    # yp(41, 1, 2)
    # yp(15, 1, 1)
    # yp(16, 1, 1)
    # yp(17, 1, 1)
    # yp(18, 1, 1)
    # yp(7, 1, 1)
    # yp(7, 2, 1)
    # yp(7, 2, 2)
    # yp(7, 2, 1)
    # yp(7, 3, 3)
    # yp(7, 3, 2)
    # yp(7, 3, 1)
    # yp(10, 5, 1)
    # yp(10, 5, 2)
    # yp(10, 5, 3)
    # yp(10, 5, 4)
    # yp(10, 5, 5)
    # yp(4, 1, 1)
    # yp(4, 2, 1)
    # yp(4, 3, 1)
    # yp(4, 4, 1)
    # yp(2, 1, 2)
    # yp(41, 1, 2)
    sys.stdout.close()

def yp(n, m, k):
    # 0<n     n elements in the circle
    # 1<=m<=n    reduce the m element after the current existing element
    # 1<=k<=n k elements remain in the circle at the end of process
    print("n =", n, " m =", m, " k =", k)
    l = [i for i in range(1, n+1)]
    i = 0
    while (len(l) > k):
        i = (i + m) % len(l)
        l.remove(l[i])
    if m == 1 and k==1:
     print("n =", n, "survive by algorithm =", l, \
           "survive by formula =", \
           int(2 * (n - math.pow(2, math.floor(math.log(n, 2)))) + 1))
    else:
        print("n =", n, "survive by algorithm =", l)
main()