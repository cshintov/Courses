""" count the number of possible substrnigs """

def count(string):
    """ count number of tuples (i, j, k) such that 
        i + j + k = num
    """
    answer = []
    num = len(string)
    for i in range(num+1):
        for j in range(num + 1):
            for k in range(num + 1):
                if i + j + k == num:
                    
                    answer.append(string[i:i+j])
    print len(set(answer))
    return list(set(answer))

print count('')
print count('a')
print count('ab')
print count('abc')
print count('abcd')
print count('abcde')
