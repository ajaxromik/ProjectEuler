def oddFunction(num):
    return 3*num + 1

def evenFunction(num):
    return num/2

def countSequence(start):
    count = 1
    while(start != 1):
        if start % 2 == 0:
            start = evenFunction(start)
        else:
            start = oddFunction(start)
        count += 1
    return count

countsList = list(map(countSequence, range(1,1000000)))
max = max(countsList)
number = countsList.index(max) + 1

print("max is {}\nthe number is {}".format(max, number))
