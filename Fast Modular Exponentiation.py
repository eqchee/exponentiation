import sys

#recursive function to implement modular exponentiation operation 
def fast_exp(m, k, n):
    #base cases
    if (m == 0): 
        return 0
    if (k == 0): 
        return 1
    #initialise r to be 0
    r = 0
    #when exponent k is even
    if (k % 2 == 0):
        r = fast_exp(m, k/2, n)
        r = (r*r) % n
    #when exponent k is odd
    else:
        r = m % n
        r = (r * (fast_exp(m, k-1, n))%n)%n
    return r

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(fast_exp(m, k, n))