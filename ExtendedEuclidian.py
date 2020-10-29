'''

 Extended Euclidean Algorithm..
 using recursive for of s and t
 S = S(i-2) - q(i-1)S(i-1)
 T = T(i-2) - q(i-1)T(i-1)
 this is for i > 2
 for i < 2, S0 = 1 and S1 = 1
            T0 = 0 and T1 = 1
 here s and t is a tuple containing
 s = (s(i-1), s(i-2)) 
 	and 
 t = (t(i-1) and t(i-2))

'''
def EEA(r0, r1, i, s ,t):
	s0, s1 = s
	t0, t1 = t
	if r0%r1 == 0:
		return (i, s, t)
	elif i < 2:
		q = r0//r1
		i, s, t = EEA(r1, r0%r1, 2, (0, 1), (1, -q))
	else:
		q = r0//r1
		s2 = s0 - q*s1
		t2 = t0 - q*t1
		i, s, t = EEA(r1, r0%r1, i+1, (s1, s2), (t1, t2))
	return (i, s ,t)


print('Enter n1 and n2: ', end='')
n = list(map(int, input().split()))

i, s, t = EEA(max(n), min(n), 1, (1, 0), (0, 1))
print('s: ', s[1], ' t: ', t[1])
