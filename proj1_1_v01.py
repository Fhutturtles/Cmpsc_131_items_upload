import math
#proj1_1_v01, kuria mbatia 11/29/2022
'''
- get angle from the user
- convert the given angle to radians
- calculate the 6 trig functions
- format 6 outputs so that it shows 4 decimal places
'''
User = float(input("Enter an angle value: "))
User = math.radians(User)
try:
    print("Value Entered in radians",format(User,'.4f'))
    print("SIN Value: ",format(math.sin(User),'.4f'))
    print("COS Value: ",format(math.cos(User),'.4f'))
    if(math.tan(User) > 1 or math.tan(User) < -1):
        print("TAN Value: Undefined")
    else:
        print("TAN Value: ", format(math.tan(User), '.4f'))
    if(1/math.sin(User) > 1 or 1/math.sin(User) < 1):
        print("CSC Value is Undefined")
    else:
        print("CSC Value: ", format(1/math.sin(User), '.4f'))
    if(1/math.cos(User) > 1 or 1/math.cos(User) < -1):
       print("SEC Value: Undefined")
    else:
        print("SEC Value: ", format(1/math.cos(User), '.4f'))
    if(1/math.tan(User) > 1 or 1/math.tan(User) < -1):
       print("COT Value: Undefined")
    else: 
        print("COT Value: ", format(1/math.tan(User), '.4f'))    
except:
    print("Error in Value printed")
