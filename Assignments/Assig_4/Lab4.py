
########################################################################
##
## CS 101 Lab
## Program #4 (Lab Week 5)
## Jeffrey Driskill
## 
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      Program functions much like a slot machine. Starting wager is requested between 1-100 after deciding amount of chips you start with 1-100
##      which moves into betting against the randint slot machine.
## 
## ERROR HANDLING:
##      While loops keep program from proceeding unless player enters correct input
##      each time input is needed.
##
########################################################################

import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play = 'a' #placeholder so while loop starts
    while play != 'NO' or play !='N' or play != 'YES' or play !='Y':#repeats if input is outside of expected bounds
        play = input('\nDo you want to play again:\n')#asks fo their input
        play = play.upper()#Puts the enitre string entered in upper case. So the input caps wont matter.
        if play == 'YES' or play =='Y':#checks the input to see if they want to play again
            return True
        elif play == 'NO' or play =='N':#checks the input if they want to play again
            return False
        else:
            print('You must enter Y/YES/N/NO. Please try again.')
            continue#restarts loop as the input was outside of bounds

def get_wager(bank : int) -> int:
    user_input = int(input('What is your wager amount?\n'))
    if (user_input) <= 0 or (user_input > bank):
        user_input = int(input('What is your wager amount?\n'))
    return user_input

def get_slot_results() -> tuple:
    reel1 = random.randint(0,10)
    reel2 = random.randint(0,10)
    reel3 = random.randint(0,10)
    tuple1 = (reel1, reel2, reel3);
    return tuple1
    ''' Returns the result of the slot pull '''

def get_matches(reela, reelb, reelc) -> int:
    if reel1 == reel2 and reel2 == reel3:
        return 3
    elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
        return 2
    else:
        return 0

def get_bank() -> int:
    user_input2 = int(input('How many chips do you want to play with?\n'))
    while user_input2 < 1 or user_input2 > 100:
        print("\nPlease enter a number between 0 and 100")
        user_input2 == int(input())
    return user_input2
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return (wager * 10) - wager
    elif matches == 2:
        return (wager * 3) - wager
    else:
        return wager * -1

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        spin = 0
        chips = bank
        totchips = bank
        

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()
            
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            

            print("\nYour spin [",reel1,'|',reel2,'|',reel3,']')
            print('------------------------')
            print("You matched |",matches,"| reels")
            print('------------------------')
            print("You won/lost [",payout,']')
            print("Current bank [",bank,']')
            print()
            spin += 1
            if totchips < bank:
                totchips = bank
           
        print("You lost all",chips,"in",spin,"spins")
        print("The most chips you had was [",totchips,']')
        playing = play_again()