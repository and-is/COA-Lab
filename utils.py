
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
