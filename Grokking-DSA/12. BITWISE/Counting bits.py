

def countBits(num):
    counter = [0]
    for i in range(1, num+1):
        b = i % 2
        a = counter[i >> 1]
        counter.append(counter[i >> 1] + i % 2)
    return counter



print(countBits(3))    