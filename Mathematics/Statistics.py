import statistics


def mean(list):
    sum = 0
    numOfElements = 0
    for i in range(len(list)):
        sum += list[i]
        numOfElements += 1
    average = sum / numOfElements
    print("Average: " + str(average))

def median(list1):
    result = statistics.median(list1)
    print("Median: " + str(result))
    
def minimum(list2):
    min = list2[0]
    for i in range(len(list2)):
        if (min > list2[i]):
            min = list2[i]
    return min

def maximum(list3):
    max = list3[0]
    for i in range(len(list3)):
        if (max < list3[i]):
            max = list3[i]
    return max

def variance(list4):
    endresult = statistics.variance(list4)
    return endresult

size = int(input("What would you like the size of your list to be? "))
l = []
for i in range(0, size):
    print("Type in element number " + str(i + 1) + ": ")
    current = int(input())
    l.append(current)
mean(l)
median(l)
print(minimum(l))
print(maximum(l))
print(variance(l))
