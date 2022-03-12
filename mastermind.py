import random
num=random.randrange(1000,10000)
print(num)
n=int(input("Guess the 4 Digits Number"))
if n==num:
    print("Great! you guessed the number in just first tyr ! You're a mastermind")
else:
    ctr=0
    while n!=num:
        ctr+=1
        count=0
        correct=['x']*4
        n=str(n)
        num=str(num)
        for i in range(0,4):
            if n[i]==num[i]:
                count+=1
                correct[i]=n[i]
            else:continue
        if count<4 and count!=0:
            print(f"you have guess {count} digits correct")
            print("Also these numbers in your input were correct.")
            for k in correct:
                print(k, end=' ')
            print('\n')
            n = int(input("Enter your next choice of numbers: "))
        elif (count == 0):
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))
        if n == num:
            print("You've become a Mastermind!")
            print("It took you only", ctr, "tries.")

