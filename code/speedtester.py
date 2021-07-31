from datetime import datetime
from getpass import getpass
from getch import getch
import pyfiglet
import time
import numpy as np

# Speed test starts
def test(k1, k2, num):
    cnt = 0

    print("\n\n\nYour test is ready. Pressing Key 1 or Key 2 will start the stopwatch.\n\n\n")

    # Loops until keys pressed = total keys 
    while cnt < num:        
        # receives keystroke
        a = getch()

        if a == k1 or a == k2:
            cnt += 1
            
            # Updates in-line counter
            print("Counter: {}".format(str(cnt)).ljust(10), end='\r')  
            
            # starts timer
            if cnt == 1:
                start = datetime.now()
                continue

        
    # Total time the test took
    total = datetime.now() - start
    total = total.total_seconds()

    print("You pressed {} times in {} seconds.".format(str(num), str(round(total, 3))))
    print("Your tapped an average of {} keys per second.".format(str(round(num/total, 3))))
    print("Your tapping speed is {} bpm.".format(str(round((num/total)*15, 3))))

    # Prints bpm to terminal with fancy text
    text = pyfiglet.figlet_format(str(round((num/total)*15, 3)))
    print(text)

    print("\n\nThis speed tester was created by Chaicow.\n\n")

    again()


# Sends total keys for test to test funciton
def keypressesmain(k1, k2):
    num = input("\n\nEnter the number of key presses for this test (10 - 10000): ")
    
    try:
        num = int(num)
    except:
        print("\nInvalid input.")
        keypressesmain(k1, k2)

    
    if num < 10 or num > 10000:
        print("\nInvalid input.")
        keypressesmain(k1, k2)

    test(k1, k2, num)


# Welcome message and determines keys to press that count as keystroke
def main():
    text = pyfiglet.figlet_format("\nChaicow")
    print(text)
    print("\n\nWelcome to Chaicow's osu! Tapping Speed Tester!\n\n")
    print("\nEnter the keys that will be used for the test.")
    print("\nPlease ONLY use letters from a-z as keys.\n")
    print("Key 1: ")
    key1 = getch()

    print("Key 2: ")
    key2 = getch()

    keypressesmain(key1, key2)


# Determines if user wants to go again
def again():
    getpass("Press enter to continue: ")

    print("\nWould you like to test again? (y/n): ")
    
    again = getch()
    if again == 'y':
        main()


main()
