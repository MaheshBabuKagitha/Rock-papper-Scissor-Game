#ROCK, PAPPER , SCISSOR
import random
MY_TOTAL_SCORE=0
YOUR_TOTAL_SCORE=0
def RPS():
    dict8={"r":"rock","p":"papper","s":"scissor","R":"rock","P":"papper","S":"scissor"}
    q=random.choice(["rock","papper","scissor"])
    print("Your choice: ",dict8[rps],"\nMy choice: ",q )
    my_score=0
    your_score=0
    global MY_TOTAL_SCORE
    global YOUR_TOTAL_SCORE
    if rps=="r" or rps=="R":
        if q=="rock":
            print("it's Tie")
        elif q=="papper":
            my_score+=1
            print("i won...")
        elif q=="scissor":
            your_score+=1
            print("You won...")
    if rps=="p" or rps=="P":
        if q=="rock":
            print("You won...")
            your_score+=1
        elif q=="papper":
            print("it's Tie")
        elif q=="scissor":
            print("i won...")
            my_score+=1
    if rps=="s" or rps=="S":
        if q=="rock":
            print("i won...")
            my_score+=1
        elif q=="papper":
            print("You won...")
            your_score+=1
        elif q=="scissor":
            print("it's Tie")
    print("\nROUND SCORE CARD >>>\t","MY SCORE =+",my_score,"   YOUR SCORE =+",your_score,"\n")
    MY_TOTAL_SCORE+=my_score
    YOUR_TOTAL_SCORE+=your_score
    print(71*"*","\nTOTAL SCORE CARD >>>\tMY_TOTAL_SCORE : ",MY_TOTAL_SCORE,"\tYOUR_TOTAL_SCORE : ",YOUR_TOTAL_SCORE,"\n",70*"*")
while True:
    rps=input("Rock - R\tPapper - P\tScissor - S\tExit - E\nChoose yours(r/p/s/e): ")
    if rps=="e" or rps=="E":
        if MY_TOTAL_SCORE > YOUR_TOTAL_SCORE:
            print(20*"#","I won , you lost. Better luck next time..",20*"#","\n")
        elif MY_TOTAL_SCORE < YOUR_TOTAL_SCORE:
            print(20*"#","You won. Congratulations..",20*"#","\n")
        else:
            print(20*"#","it's Tie. so,we both won..",20*"#","\n")
        break
    elif rps not in ["r","p","s","R","P","S"]:
        print("Oops..! chose correctly :)\n")
    else:
        RPS()
        print("Will play again..")