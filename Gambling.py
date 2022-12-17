import random
import os

MAX_BET = 100
MIN_BET = 1

reels = [[' A ',' B ',' C '],[' A ',' B ',' C '],[' A ',' B ',' C ']]

# To deposit the money in the slot machine.
def deposit():
    while True:
        amount = input("How much amount would you like to deposit ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Print a valid amount greater than 0. ")
        else:
            print("Print a valid amount. ")
    return amount

# To make a bet
def make_bet():
    while True:
        amount = input("How much amount would you like to bet ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Print a valid amount between {MIN_BET} & {MAX_BET}. ")
        else:
            print(f"Print a valid amount between {MIN_BET} & {MAX_BET}. ")
    return amount

# To spin the slot machine
def spin():
    SpinResult = ''
    for reel in reels:
        SpinResult += str(random.choice(reel))
    return SpinResult

# To check if the player wins or not
def luck_check(Onscreen):
    Onscreen_set = set(Onscreen)
    if len(Onscreen_set) == 2:
        return True
    else:
        return False
    

def main():
    print("\nGAMBLING INVOLVES RISK. PLEASE ONLY GAMBLE WITH FUNDS THAT YOU CAN COMFORTABLY AFFORD TO LOSE..\n")
    balance = deposit()
    cont = True
    while cont:
        betamount = make_bet()
        OnScreen = ""
        if betamount <= balance:
            OnScreen = spin()
        else:
            print("Insufficient Balance ! Please make a valid Bet. ")
            betamount = make_bet()        
        print("SLOT MACHINE DISPLAY : " + "["+OnScreen+"]") 
        luck = luck_check(OnScreen)
        if luck:
            balance = (balance - betamount) + (betamount*2)
        else:
            balance = balance - betamount
            print("BAD LUCK")   
        print(f"Now your Current deposited amount = ${balance}")
        if balance >= 1:
            temp = input("\nPress E for exit or Press any ENTER or ANY to continue Playing : ")
            if temp == 'E':
                cont = False
            else:
                os.system('cls')
                print(f"Left Amount : ${balance}")
        else:
            # os.system('cls')
            print("\nYou have $0 in your account. \n     YOU LOST ! \n   OH, BAD LUCK !")
            cont = False
               
main()
