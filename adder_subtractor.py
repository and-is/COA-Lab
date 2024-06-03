import utils

def makeEqual(a,b):
    if(len(a)>len(b)):
        for i in range(0,len(a)-len(b)):
            b = '0'+ b
    elif(len(a)<len(b)):
        for i in range(0,len(b)-len(a)):
            a = '0' + a
    return (a,b)

def adder(input1, input2):
    (input1,input2)=makeEqual(input1, input2)
    input1 = input1[::-1]
    input2 = input2[::-1]
    summ = ''
    carry = '0'
    for i in range(0,len(input1)):
        carry = carry + utils.findCarry(input1[i],input2[i],carry[i])
        summ = summ + utils.findSum(input1[i],input2[i],carry[i])
    summ = summ + carry[len(carry)-1]
    return summ[::-1]

def onesComp(a):
    b=''
    for i in range(len(a)):
        if(a[i]=='0'):
            b = b + '1'
        else:
            b = b + '0'
    return b

def twosComp(a):
    return adder(onesComp(a),'0001')

def subtractor(a,b):
    return adder(a,twosComp(b))
