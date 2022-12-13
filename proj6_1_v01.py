from statistics import mean

filez1 = open('z1.txt', 'r')
setz1 = set([])
for line in filez1:
    value = float(line) #data is automatically read
    setz1.add(value)

filez2 = open('z2.txt', 'r')
setz2 = set([])
for line in filez2:
    value = float(line) #data is automatically read
    setz2.add(value)

meanz1 = mean(setz1)
print("the mean is of the first set is: ")
print(format(meanz1,'.3f'))

print("")

meanz2 = mean(setz2)
print("the mean is of the second set is: ")
print(format(meanz2,'.3f'))

sameVals = set(setz1).intersection(setz2)
print("")
print("The following are the values that appear in both sets: ")
print(sameVals)
print("In total there are 9 values that appear in both sets")