# Uses python3
import sys
def gcd_naive(a, b):
    r = a%b
    q = int(a/b)
    while(r!=0):
        a = b
        b = r
        q = int(a/b)
        r = a - (b * q)
    return(b)
def lcm(a, b):
    return int(a * b / gcd_naive(a, b))
    
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
