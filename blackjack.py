# num = int(input("Please input a number between 1 and 100: "))
# while num > 100:
#     print("That is not a valid number.  Please try again.")
#     num = int(input("Please input a numberbetween 1 and 100: "))
#     if num < 100: 
#         continue
# if num < 49:   
#      print("The value you entered is lower than 49")
# elif num > 50: 
#     print("The value you entered is higher than 50")
# elif num < 50: 
#     print("The value you entered is lower than 50")
# else:
#      print("The value you entered is 50")
import random
num = int(random.randrange(2,21))
print(num)

    
while num < 21:
    print("The number is less than 21.")
    print("Would you like another card?")
    
    dealer_ask = input("Y/N:")  
    
    if dealer_ask.upper() == "Y":
        draw_card = int(random.randrange(1,11))
        num += draw_card
        print(f"You drew a {draw_card}. Your total is now {num}.")
    elif num > 21: 
        print("The number is higher than 21, you busted.")   
    elif num (21):  
        print("BLACKJACK!")
    else:  
        print(f"Your hand is {num}")
