import math
def is_prime(N):
    if N<2:
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def eratos_1(size):
    listt = [True]*size
    listt[0] = False
    listt[1] = False

    for i in range(2,size):
        for j in range(2,int((size)/i)+1):
            if listt[i] == True:
                pointer = i*j
                while(pointer < (size)):
                    listt[pointer] = False
                    pointer += j

    prime = []
    for i in range(size):
        if listt[i] == True:
            prime.append(i)

    return prime
    


size = int(input("enter integer no.: "))
prime1 = eratos_1(size)
for i in range(len(prime1)):
    print(i,"        ",prime1[i],"   ",is_prime(prime1[1]))
