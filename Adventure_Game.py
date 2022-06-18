import time
from termcolor import colored

print('''
           *** DEMO GAME ***
            MADE BY : NATCHO
''')
time.sleep(2)

a = input("Start Game ? : ").lower()
if a == "yes":
    print("\033c")
    print('''
    DATE :
    01/03/2020

    INFORMATIONS ABOUT YOUR CHARACTER : 

    Name : POLO
    Age : 31
    current year : 2020

    INVENTORY :

    cigarette
    phone
    Medical Equipment

    MONEY : 
    80$
    ''')
    input("Press Enter to continue...")
    print("\033c")
    print("On That day I was going to work but I bumped into someone on my way ...")
    time.sleep(3)
    print("Unknown : Hi Man Can You Help Me Please ?")
    time.sleep(2)
    print("You : Hi , Excuse Me can I know who are you ?")
    time.sleep(2)
    print("Unknown : Im Brade.")
    time.sleep(2)
    print("You : Sure How can I Help You, Brade ?")
    time.sleep(2)
    print("Brade : I have some cocaine in my pocket and I want to sell it, can you sell it for me and I'll give you half of the money.")
    print("\n1) Yes I Really Need Money !")
    print("2) No I can't Do That !")
    print("3) Call 911")
    b = int(input("Choose one of the options (1, 2, 3) : "))
    if b == 1:
        print("\nYou : Yes , I Really Need Money ")
        time.sleep(2)
        print("Brade : So Good , Now take this 300g of cocaine.")
        time.sleep(2)
        print(colored('*300g cocaine Added to inventory*', 'green'))
        time.sleep(3)
        print("Brade : Now if you sell it, come over here and we split the money.")
        print("\n1) Okay")
        print("2) No, I'll take all the money on my own ")
        c = int(input("Choose one of the options (1, 2) : "))
    elif b == 2:
        print("Brade : WHAT!!! , Are You Sure About That ?")
        time.sleep(3)
        print(colored("Wait For The Complete Game :)","red"))
        print(colored("That's Just DEMO \nComplete Version Will Be Done soon...","yellow"))
        time.sleep(5)
        exit()
    elif b == 3:
        print("Brade : What Are You doing in your phone ?!")
        time.sleep(3)
        print(colored("Wait For The Complete Game :)","red"))
        print(colored("That's Just DEMO \nComplete Version Will Be Done soon...","yellow"))
        time.sleep(5)
        exit()
    if c == 1 or c == 2:
        print(colored("Wait For The Complete Game :)","red"))
        print(colored("That's Just DEMO \nComplete Version Will Be Done soon...","yellow"))
        time.sleep(5)
        exit()
        
elif a == "no":
    print("Okay , See You Later Bro :D")
    time.sleep(2)
    print(colored("That's Just DEMO \nComplete Version Will Be Done soon...","yellow"))
    time.sleep(5)
    exit()
else:
    print("Invalid Answer! , try : (yes / no)")   