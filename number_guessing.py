import random
import time

minesanas_intervals = 100

sakuma_laiks = time.time()


computer_guessed_number = random.choice(range(0,minesanas_intervals))
def number_guess():
    count = 0
    while True:
        guess = input(f"Uzmini skaitli no viens līdz {minesanas_intervals}: ")
        if computer_guessed_number == int(guess):
            print("Ir pareizi!")
            print(f"Kopā minēji {count} reizes!")
            hronometrs = round((time.time() - sakuma_laiks), 1)
            print(f"Minēji {hronometrs} sekundes!")
            break
        else:
            if int(guess) > computer_guessed_number:
                print("Cipars par lielu")
                print("Mini atkal!\n-----------")
            elif int(guess) < computer_guessed_number:
                print("Cipars par mazu")
                print("Mini atkal!\n-----------")
                count = count + 1

number_guess()
velreiz = input("Spēlēsi vēlreiz: ")
if velreiz == "jā":
    print("-----------")
    number_guess()
else: 
    print("-----------\nSpēle ir beigta!")
    
    
