import utils
import adder_subtractor

def booth_multiplication(m, q):
    n = len(q)
    q_ = '0' * len(m)
    A = q_ + q + '0'
    print(A)
    S = adder_subtractor.twosComp(m)

    for i in range(n):
        print(A[-2:])
        B = A[len(m):-1]
        print(B)
        if A[-2:] == '01':
            A = adder_subtractor.adder(A[:-(n+1)], m) + B
        elif A[-2:] == '10':
            A = adder_subtractor.adder(A[:-(n+1)], S) + B
        else:
            A = A[0] + A[:-1] 
        print("After ASR "+A)
    
    return A[:-1]

print(booth_multiplication("1011", "0100"))

