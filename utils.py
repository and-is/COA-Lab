def reverse(input1):
    return input1[::-1]

def andGate(a,b):
    if(a=="1" and b=="1"):
        return "1"
    else:
        return "0"

def orGate(a,b):
    if(a=="0" and b=="0"):
        return "0"
    else:
        return "1"

def xorGate(a,b):
    if(a==b):
        return "0"
    else:
        return "1"

def findSum(a,b,c):
    return xorGate(xorGate(a,b),c)

def findCarry(a,b,c):
    return orGate(orGate(andGate(a,b),andGate(b,c)),andGate(a,c))

def onesComp(a):
    b=''
    for i in range(len(a)):
        if(a[i]=='0'):
            b = b + '1'
        else:
            b = b + '0'
    return b

def twosComp(a):
    b = adder(onesComp(a),'0001')
    return b[1:]

def adder(input1, input2):
    (input1,input2)=makeEqual(input1, input2)
    input1 = input1[::-1]
    input2 = input2[::-1]
    summ = ''
    carry = '0'
    for i in range(0,len(input1)):
        carry = carry + findCarry(input1[i],input2[i],carry[i])
        summ = summ + findSum(input1[i],input2[i],carry[i])
    summ = summ + carry[len(carry)-1]
    return summ[::-1]

def subtractor(a,b):
    sub = adder(a,twosComp(b))
    return sub[1:]

def makeEqual(a,b):
    if(len(a)>len(b)):
        for i in range(0,len(a)-len(b)):
            b = '0'+ b
    elif(len(a)<len(b)):
        for i in range(0,len(b)-len(a)):
            a = '0' + a
    return (a,b)

#print(adder(adder(adder('1011000','101100'),''),'1011'))
