def bubblesort(array):
    n = len(array)
    for i in range(n - 1):
        for k in range(0, n - i - 1):
            if(array[k] > array[k + 1]):
                array[k], array[k + 1] = array[k + 1], array[k]
    print("Sorted array: ")
    print(array)

length = int(input("What would you like the size of your array to be? "))
l = []
for i in range(0, length):
    print("Type in element number " + str(i + 1) + ": ")
    current = int(input())
    l.append(current)
bubblesort(l)