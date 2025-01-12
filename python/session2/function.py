def extractsentnce(test):
    arr = test.split('.')
    numofarr = len(arr)
    return arr, numofarr

output, num = extractsentnce('test . new . test')
print(output)
print(num)