import math

def hash_map(txt):
    ans = 0
    for i in range(len(txt)):
        ans = ans * 26 + ord(txt[i]) - ord('A') + 1
    return ans

def unhash_map(n):
    s = []
    while n > 0:
        s.append(chr((n - 1) % 26 + ord('A')))
        n //= 26
    return ''.join(s[::-1])
    

def nghichdao(a, b):
    m = b
    x1, x2 = 0, 1
    while b > 0:
        q = a // b
        r = a % b
        x = x2 - x1 * q
        x2, x1 = x1, x
        a, b = b, r
    while x2 < 0:
        x2 += m
    return x2

def pow_mod(a, b, n):
    a %= n
    ans = 1
    if b == 0:
        return 1
    while b > 0:
        if b % 2 == 1:
            ans = (ans * a) % n
        a = (a * a) % n
        b //= 2
    return ans

def pt_mod(a, b, n):
    # c = nghichdao(a, n)
    d = pow_mod(a, n - 2, n)
    return (b * d ) % n

def thangdubac2(a, p):
    return pow_mod(a, p // 2, p) == 1

def point_in_elliptic(m, a, b, p):
    x = (m**3 + a*m + b) % p
    return thangdubac2(x, p)

def find_thangdubac2(m, a, b, p):
    x = (m**3 + a*m + b) % p
    return pow_mod(x, (p+1)//4, p)

def str_cs2(n):
    s = []
    while n > 0:
        s.append(chr(n % 2 + ord('0')))
        n //= 2
    return ''.join(s[::-1])

def add_point(P, Q, a, b, p):
    if P == [0, 0]:
        return Q
    if Q == [0, 0]:
        return P
    if P[0] == Q[0] and (P[1] + Q[1]) % p == 0:
        return [0, 0]
    
    if P == Q:
        lamda = pt_mod(2 * P[1], 3 * P[0] * P[0] + 2 * a * P[0] + b, p)
    else:
        lamda = pt_mod(Q[0] - P[0], Q[1] - P[1], p)
    
    first = lamda * lamda - P[0] - Q[0]
    second = lamda * (P[0] - first) - P[1]
    return [first % p, second % p]

def mul_k_point(P, k, a, b, p):
    if k <= 0:
        return [0, 0]
    s = str_cs2(k)
    T = P
    for i in range(1, len(s)):
        T = add_point(T, T, a, b, p)
        if s[i] == '1':
            T = add_point(T, P, a, b, p)  
    return T

def neg(P):
    return [P[0], -P[1]]

# print(str_cs2(2583))
# s = "ABCDZ"
# a = hash_map(s)
# print(a)
# b = unhash_map(a)
# print(b)

    