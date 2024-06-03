import utils

def multiply(multiplicand, multiplier):
    array = []
    n = len(multiplier)
    for i in range(0,n):
        str1 = '0000'
        if multiplier[i]=='1':
            str1 = multiplicand
        for i in range(0, n-i-1):
            str1 = str1 + '0'
        array.append(str1)
    print(array)
    product=''
    for i in range(0,len(array)):
        product = utils.adder(array[i],product)
        print(product)
    return product

print('Product is ' + multiply('101','011'))

