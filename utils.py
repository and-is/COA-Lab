m = input("Enter the multiplicand: ")
q = input("Enter the mutliplier: ")

if(len(m)>len(q)):
    max_len = len(m)
else:
    max_len = len(q)

#adding zeros at front if the length are not same
m = m.zfill(max_len)
q = q.zfill(max_len)

def XOR(a,b):
    if((a == 0 and b == 0) or (a == 1 and b == 1)):
        return 0
    else:
        return 1

#implementation of full adder
def add(a,m):
    result = ""
    carry = 0
    for i in range(max_len - 1, -1, -1):
        result += str(XOR(XOR(int(a[i]), int(m[i])), int(carry)))
        if( m[i] == '1' and a[i] == '1'):
            carry = '1'
        elif((carry == '1') and ((m[i] == '1') or (a[i] == '1'))):
            carry = '1'
        else:
            carry = '0'
              
    return(result[::-1], carry)

#implementation of right shift
def right_shift(a , q, sign_bit):
    string = a + q
    string = string[:-1] #remove last character from the string
    string = sign_bit + string # insert character at the beginning
    return(string)

def mutliplication(m, q):
    a = ""
    a = a.zfill(max_len)
    for i in range(max_len - 1, -1, -1):
        if(q[max_len -1] == '0'):
            result = right_shift(a,q,'0')
            a = result[0:4]
            q = result[4:8]
        else:
            a,carry = add(a,m)
            result = right_shift(a,q, carry)
            a = result[0:4]
            q = result[4:8]
    return(a,q)
       
a,q = mutliplication(m,q)
print(a+q)
 
