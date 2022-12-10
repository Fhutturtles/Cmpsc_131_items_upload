#Kuria Mbatia, proj2_1_v01, 12/7/2022
a1 = float(input("Please enter a x1 value: "))
b1 = float(input("Please enter a y1 value: "))
a2 = float(input("Please enter a x2 value: "))
b2 = float(input("Please enter a y2 value: "))
    #FInd slope 
    #Check if slope is horizontal, vertical, positive, negative, or even if there is no slope at all (edge case it's just the same point)
p1 = b2-b1
    #if this is equal to zero then the slope is zero
p2 = a2-a1
if(p2 == 0):
    if(p1 == 0):
        print("There is no slope, point is static")
    else:
        print("The slope is vertical")
else:
    if(p1 == 0 and p2 != 0):
        print("The slope is horizontal")
    else:
        if((p1/p2) > 0 ):
            print("The slope is Positive " +str(p1/p2))
        else:
            if((p1/p2) < 0 ):
                print("The slope is negative " +str(p1/p2))
