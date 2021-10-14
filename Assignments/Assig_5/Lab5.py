########################################################################
##
## CS 101 Lab
## Program # 5
## Name:Jeffrey Driskill
## Email: jtdgz8@umkc.edu
##
## PROBLEM : Check digit program for Linda Hall library. 
##
## ALGORITHM : 
##      1. Enter library card value
##      2. Based on entry check get_school and grade of student
##      3. If invlaid return error message, and allow for re-entry
##      4. allow for re-entry after school/grade is printed
##      5. Rince, repeat, re-entry
##      6. Hit enter to end loop
## 
##
########################################################################


import string


def character_value(c : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    value = ord(c)
    if (value >= 48 and value<=57):
        return value - 48
    elif (value >= 65 and value<=90):
        return value - 65
    

def get_check_digit(lib_card : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    sum = 0
    for i in range(len(lib_card)):
        value = character_value(lib_card[i])
        sum += value * (i+1)
    return sum % 10

def is_valid(lib_card : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    while(1):
        lib_card = input("Enter Library Card. Hit Enter to Exit ==> ")
        (valid,msg) = verify_check_digit(lib_card)
        
        if valid == True:
            print(msg)
            print("The card belongs to a student in " + get_school(lib_card))
            print("The card belongs to a " + get_grade(lib_card))
                
        else:
            print("Library card is invalid.")
            print(msg)
    

def verify_check_digit(lib_card : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    if len(lib_card) != 10:
        return (False,"The length of the number given must be 10")
        
    for i in range(5):
        if lib_card[i] < 'A' or lib_card[i] > 'Z':
            msg = "The first 5 characters must be A-Z, the invalid character is at index " \
            + str(i) +" is " + lib_card[i]
            return (False, msg)
    
    for i in range(7,10):
        if lib_card[i] < '0' or lib_card[i] > '9':
            msg = "The last 3 characters must be 0-9, the invalid character is at index "\
                    + str(i) +" is " + lib_card[i]
            return (False, msg)
    if (lib_card[5] != '1' and lib_card[5] != '2' and lib_card[5] != '3'):
            return (False, "The sixth character must be 1,2 or 3")
    
    if (lib_card[6] != '1' and lib_card[6] != '2' \
        and lib_card[6] != '3' and lib_card[6] != '4'):
            return (False, "The seventh character must be 1,2,3 or 4")
    
    calculated_value = get_check_digit(lib_card)
    num = int(lib_card[9])
    
    if num != calculated_value:
        msg = "Check digit " + str(num) + " does not match calculated value " \
               + str(calculated_value)
        return (False,msg)
        
    return (True,"Library card is valid.")

def get_school(lib_card : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    if lib_card[5] == '1':
        return "School of Computing and Engineering SCE"
    elif lib_card[5] == '2':
        return "School of Law"
    elif lib_card[5] == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"
  

def get_grade(lib_card : str) -> str:
    '''Returns the grade for index 6'''
    if lib_card[6] == '1':
        return "Freshman"
    elif lib_card[6] == '2':
        return "Sophomore"
    elif lib_card[6] == '3':
        return "Junior"    
    elif lib_card[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"
   

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        lib_card = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if lib_card == "":
            break
        result, error = verify_check_digit(lib_card)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(lib_card)))
            print("The card belongs to a {}".format(get_grade(lib_card)))
        else:
            print("Libary card is invalid.")
            print(error)
        