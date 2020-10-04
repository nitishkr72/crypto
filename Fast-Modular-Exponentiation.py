'''
    Using repeated Squaring modulo to
    calculate modular exponentiation
    function uses:
        CalcSmallExpo(memo, A, B, C)
            it will do all smaller modular exponentiation
        get2PowerN(B)
            it is a helper function to calculate B in
            form of sum of power of 2's
        inBinaryGet(B)
            calculate B in form of sum of power of 2's
        repSqrModN(A, B, C)
            it will divide the B into smaller and use
            calcSmallExpo() to calculate smaller modular
            exponent and combine it as follows
            ((a mod b)*(c mod b)*(d mod b)) mod b =
                (e*f*g) mod b
        main()
            main driver function
'''
def CalcSmallExpo(memo, A, B, C):
    if B in memo:
        return memo
    elif B==1:
        memo[B] = A%C
        return memo
    else:
        memo = CalcSmallExpo(memo, A, int(B/2), C)
        n = memo[int(B/2)]
        memo[B] = (n*n)%C
        return memo

def get2PowerN(B):
    if(B==1):
        return 1
    i = 1
    while(i<=B):
        i = i*2
    return int(i/2)

def inBinaryGetB(B):
    ls = []
    while(B>0):
        num = get2PowerN(B)
        B = B-num
        ls.append(num)
    return ls

def repSqrModN(A, B, C):
    ls = inBinaryGetB(B)
    memo = {}
    CalcSmallExpo(memo, A, ls[0], C)
    result = 1
    for b in ls:
        result = result*memo[b]
    return result%C

def main():
    print("Repeated Modulo Multiplication to Calculate modular exponentiation")
    print("A^B mod C = repSqrModN(A, B, C)")
    print("Enter the Value of A, B, C")
    A = int(input())
    B = int(input())
    C = int(input())

    result = repSqrModN(A, B, C)
    print("{}^{} mod {} = {}".format(A, B, C, result))

main()
