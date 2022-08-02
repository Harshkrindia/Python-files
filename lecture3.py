# h= int(input())
# if (h>10):
#     print("The number is grater then 10")
# elif(h<10):
#     print("The number is less than 10")
# else:
#     print("Equal")

# while(h>10):
#     print("I am greater than 10")
#     h=h-5

    # The above things was deleted by haman bhaiya for a clean thing but i will not remove it as it would help me later.

       # The following this is a game of guessing a random number selected by the computer.

import random
r = random.randint(1,1000)
# 
print("Guess a number(•_•)")
# 
while(True):
    inp = int(input())
    if(inp<r):
        print("Wrong guess, try a greater number :D")
    elif(inp>r):
        print("Wrong guess, try a smaller number :-)")
    else:
        print("Congrats! You guessed it right:-D")
        break;
