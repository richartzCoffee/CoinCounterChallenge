from module import coin


def display():

    print("""
__________Computer vision challenge - Counting coins__________
    """)
    while(True):
        print("""
     _______________________________
    |__________Coin Counter_________|
    |                               |        
    |   Choice an option            |
    |                               |
    |   1 - Counting Real Coins     |
    |                               |
    |   2 - Counting Dollar Coins   |
    |                               |
    |   0 - exit the program        |
    |_______________________________|
        """)
        option_user = str(input("Option >> "))

        if(option_user == "0"):
            break
        elif(option_user == "1"):
            coin.coinReal()
        elif(option_user == "2"):
            coin.coinDolar()
        else:
            print("""
            ___invalid option___

            please,try again
            """)
