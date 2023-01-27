import random


for i in range(10):
    a=random.randint(1,11)
    b=random.randint(1,11)

    print("Q",i+1,')          ',a,"*",b,"=","\n")
    n1=int(input())
    if(n1==a*b):
        print("                    RIGHT ANSWER")
    else:
        print("                    WRONG ANSWER","\n","RIGHT ANSWER ",a*b)