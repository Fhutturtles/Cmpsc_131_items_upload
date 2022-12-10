'''
example 
rows: 2 columns: 5 number of fields 4
***** ***** ***** *****
***** ***** ***** *****
'''
User_Rows = int(input("Enter the number of rows: "))
User_Cols = int(input("Enter the number of Columns: "))
User_Fields = int(input("Enter the number of Fields: "))
if((User_Rows <= 5 and User_Rows >= 1) and (User_Cols >= 5 and User_Cols <= 50 ) and (User_Fields <= 10 and User_Fields >= 3)):
    Custom = str(input("Would you like a custom value to set as the array letter? Enter 'Y' or 'N' to continue: "))
    if(Custom == "Y"):
        pattern = str(input("Enter your Custom letter value: "))
        arr_in = [pattern] * User_Cols
        arr_out = [arr_in] * User_Fields
        for val in range(0,User_Rows):
            print(arr_out)
            print('\n' * 3)
            #print('\n' * 40)
    else:
        arr_in = ["*"] * User_Cols
        arr_out = [arr_in] * User_Fields
        for val in range(0,User_Rows):
            print(arr_out)
            print('\n' * 3)
            #print('\n' * 40)
