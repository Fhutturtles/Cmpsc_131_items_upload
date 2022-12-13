n=20
lst = []
print("This program will let you input 20 numbers and return the average of your numbers.")
print("Then it will display the closest and furthest number to said average.")
print("Please enter your 20 values below:")
print("")
for i in range(0, n):
    ele = int(input("Please Enter Value: "))
    lst.append(ele)
print("")
print("-----------------------------------")
print("")
print("Your numbers are: ", lst)
ave = sum(lst) / len(lst)
lst.append(ave)
sortedlist = lst.sort()
print("Your numbers in order are: ", lst)
print("The averge of your numbers is: ", ave)
print("")
indexave = lst.index(ave)
indexAbove = indexave+1
indexBelow = indexave-1
biggernumber = lst[indexAbove]
smallernumber = lst[indexBelow]
distAbove = lst[indexAbove] - lst[indexave]
distBelow = lst[indexave] - lst[indexBelow]
if distAbove>distBelow:
    print("The closet number to", ave, "is ", smallernumber)
elif distAbove<distBelow:
    print("The closet number to", ave, "is ", biggernumber)
elif distAbove==distBelow:
    print("The average is of equal distance to", smallernumber, "and ", biggernumber,)   
print("")
indexFirst = lst[0]
indexLast = lst[20]
distFirst = lst[indexave] - indexFirst
distLast = indexLast - lst[indexave]
biggestnumber = indexLast
smallestnumber = indexFirst
if distFirst>distLast:
    print("The farthest number to", ave, "is ", smallestnumber)
elif distFirst<distLast:
    print("The farthest number to", ave, "is ", biggestnumber)
elif distAbove==distBelow:
    print("The average is of equal distance to", smallestnumber, "and ", biggestnumber,)