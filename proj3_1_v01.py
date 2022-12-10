#Enable user to be able to continue doing while loop essentially limit is 20 values input
#tell user to enter a value
import numpy
arr = []
count  = 0
Continuity = "True"
while(Continuity == "True" and count < 20):
    print("Please Enter a numerical Value, if it is negative it will be changed to positive!")
    send = int(input("Please enter a value: "))
    if(send < 0):
        send = send*-1
    arr.append(send)
    Continuity = str(input('Would you like to continue? Type "True" or "False" to continue: '))
    if(count == 20):
        print("You cannot enter any more values")

#Calculate the average of the values 
total_evens = 0
count_evens = 0
total_odds = 0
count_odds = 0
for val in arr:
    if(val%2==0):
        total_evens = total_evens + val
        count_evens+=1
    else:
        total_odds = total_odds + val
        count_odds+=1
print("Averages of even was input: " + str(total_evens/count_evens))
print("Averages of odds was input: " + str(total_odds/count_odds))