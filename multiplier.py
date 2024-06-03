import utils
import adder_subtractor

def multiply(multiplicand, multiplier):
    array = []
    n = len(multiplier)
    for i in range(0,n):
        str1 = ''
        if multiplier[i]=='1':
            str1 = multiplicand
        for i in range(0, n-i-1):
            str1 = str1 + '0'
        array.append(str1)
    product=''
    for i in range(0,len(array)):
        product = adder_subtractor.adder(array[i],product)
    return product
