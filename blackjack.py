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
