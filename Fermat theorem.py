'''
			CSB18040  
'''

import random
##########################################################
##########################################################
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
##########################################################
def get2PowerN(B):
    if(B==1):
        return 1
    i = 1
    while(i<=B):
        i = i*2
    return int(i/2)
##########################################################
def inBinaryGetB(B):
    ls = []
    while(B>0):
        num = get2PowerN(B)
        B = B-num
        ls.append(num)
    return ls
##########################################################
def repSqrModN(A, B, C):
    ls = inBinaryGetB(B)
    memo = {}
    CalcSmallExpo(memo, A, ls[0], C)
    result = 1
    for b in ls:
        result = result*memo[b]
    return result%C
##########################################################
########end-of-repeated-squaring-method###################



'''
	using fermat theorem to find whether N is prime or not
	here a is 2 < a < N-1
		and for all a, 
				if a^N-1 mod N == 1
					then N is prime
				else N not prime...
	fermat theorem is implemented in isPrime(N) function.
'''
def isPrime(N):
    a = 2
    while(a<N-1):
        if(repSqrModN(a, N-1, N)!=1):
            return False
        a = a+1
    return True

def main():
    #num = 97
    num = random.getrandbits(63)
    if isPrime(num):
        print("{} is a prime number".format(num))
    else:
        print("{} is not a prime number".format(num))

print("number greater than 2**63 and is randomly generated")
main()
