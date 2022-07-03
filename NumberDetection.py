l = [1, 20, 40, 30, 2, 5, 4]
status = False

for i in range(len(l)):
    if l[i] == 30:
        status = True

if(status == True):
    print("30 is in this list")
else:
    print("30 is not in this list")