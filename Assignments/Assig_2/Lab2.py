'''
Jeffrey Driskill
CS101L
Fall21 - M - 7-9:30
'''

while True:                            
    print('Please think of a number between and including 1 and 100. \n') 
    nums = '357'                      
    result = [ ]                                       
    for i in nums:                    
        while True:
            print('What is the remainder when your number is divided by', i,'? ', end='')
            f = int(input())
            if (f >= int(i)):
                print('The value entered must be less than', i)
                continue
            if (f < 0):
                print('The value entered must be 0 or greater')
                continue
            else:
                if(f != '7'):
                    print()
                result.append(f)
                break                         


    for number in range(1,101):
        if number % 3 == result[0]:
            if number % 5 == result[1]:
                if number % 7 == result[2]:
                    print('Your number was',number)
                    print('How amazing is that?')
                    break
                else:
                    continue
            else:
                continue
        else:
            continue                                      
    
    while True:
        answer = ''                 
        print('Do you want to play again? Y to continue, N to quit ==>')
        answer = input()
        if answer == 'Y' or answer =='y' or answer == 'N'or answer == 'n':
            break
        else:
            continue

    if answer == 'N' or answer == 'n':
        break
    elif answer == 'Y' or answer == 'n':
        print()
        continue