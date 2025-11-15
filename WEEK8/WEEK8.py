''''
#function --builtin --user defined
from itertools import count


#function with parameter, no return
def get_the_sum(input1, input2):
    sum =  input1 + input2
    print(sum)

a = 25
b = 18
get_the_sum(a, b)

a = 34
b = 35
get_the_sum(a, b)

#function with parameter and return
def get_the_sum(input1, input2):
    sum =  input1 + input2
    print(sum)
    return sum

a = 21
b = 41
c = 61
d = 67

print(get_the_sum(a, b) + get_the_sum(c, d))

#function with no parameter and no return
import time
def countdown():
    print("Counting down: ")
    for i in range(100, 0, -1):
        time.sleep(0)
        print(i)
    print("Countdown Finished!")
countdown()
'''

import time
import os

Amount = 0
Balance = 6490
Pin = "123456"


def Welcome_Message():
    print("_ _ _ _ _ _ _ _ _ _")
    print("Welcome To Our Precious bank")
    print("- - - - - - -")
    print("Enter Your Card")

def Card_Reader(CardIsInserted):
    if CardIsInserted == "Yes":
        print("Your card is inserted")
        return True
    else:
        print("Your card is NOT inserted")
        return False

def Pin_No():
    for i in range(4):
        if i == 3:
            print("Your Card Is Blocked, Contact Your Bank")
            return False
        EnterPinNumber = input("Enter the Pin Number: ")
        if EnterPinNumber == Pin:
            return True
        else:
            print("Pin Number Error")

def transaction_selection():
    transaction = input("Which transaction would you like to do?")
    return transaction

def transaction_validation(Amount, Balance):
    if Balance >= Amount:
        return True
    else:
        print("Not Enough Balance")
        return False

def card_ejection():
    print("Card Ejection")

def cash_dispensing():
    print("Cash dispensing, Please Wait...")

def print_receipt():
    global Balance
    Balance = Balance - amount
    print("Your Remaining Balance is:", Balance)
    print("Amount Witdrawn: ", amount)
    print("Get Your Receipt, Please.")

while True:
    Welcome_Message()
    CardIsInserted = input("Is The Card Inserted? (Yes/No)?")
    if not Card_Reader(CardIsInserted):
        continue
    print("Next Step")
    if not Pin_No():
        continue
    print("Next Step")

    if transaction_selection() == "Withdraw":
        amount = int(input("Enter Amount: "))
        if transaction_validation(amount, Balance):
            print("Withdraw Transaction")
            card_ejection()
            cash_dispensing()
            print_receipt()
        else:
            card_ejection()
            continue

    elif transaction_selection() == "Check Balance":
        print("Your Balance is:", Balance)
    else:
        continue







