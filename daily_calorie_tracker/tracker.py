# JAI KASHYAP, 03/10/2025, DAILY CALORIE TRACKER

from datetime import datetime
import csv

def main():
    print("WELCOME TO THE JK CALORIE TRACKER!\n") # TASK 1

    mealNum = int(input("HOW MANY MEALS DO YOU WANT TO TRACK TODAY?: "))
    meals, mealsCals = [], []

    for i in range(mealNum): # TASK 2
        mealInput = input("\nENTER MEAL NAME: ")
        while len(mealInput) > 9: # CHARACTER LIMIT SO THAT FORMATTED OUTPUT IS NEATER
            print("\nYOU HAVE EXCEEDED THE CHARACTER LIMIT")
            mealInput = input("\nENTER MEAL NAME: ")
        
        meals.append(mealInput)
        mealsCals.append(int(input("\nENTER {}'S CALORIE AMOUNT: ".format(meals[i]))))

    totalCals = sum(mealsCals) # TASK 3
    averageCals = totalCals/mealNum

    calLimit = int(input("\nDEAR USER, PLEASE ENTER YOUR DAILY CALORIE LIMIT: "))
    evaluation = None # DETERMINES WHETHER USER HAS EATEN UNDER/OVER CALORIE LIMIT FOR BONUS TASK

    if totalCals > calLimit: # TASK 4
        print("\nOH NO! IT SEEMS LIKE YOU'VE PASSED YOUR CALORIE LIMIT.")
        evaluation = False
    else:
        print("\nCONGRATULATIONS! YOU'VE EATEN ACCORDING TO YOUR CALORIE LIMIT.")
        evaluation = True

    print("\nMeal Name   Calories") # TASK 5
    print("-" * 25)
    for i in range(mealNum):
        print(f"{meals[i]}" + " "*(12-len(meals[i])) + f"{mealsCals[i]}")
    print(f"TOTAL: {totalCals}")

    permission = input("ENTER 1 IF YOU WANT TO REPORT YOUR DATA TO THE FILE: ") # TASK 6
    if permission == '1':
        with open('calTracker.txt','a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), meals, totalCals, averageCals, evaluation])
        file.close()
    else:
        pass
    print("\nTHANK YOU FOR USING THE JK CALORIE TRACKER :)")

if __name__ == '__main__':
    main()