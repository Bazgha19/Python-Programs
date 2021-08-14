# Rock Paper Scissors
'''
import random

name=input('Enter your name:')
print('Welcome',name,' to the RPS game!!!')
print('Enter your choice')
a=input("'r' for rock, 'p' for paper, 's' for scissors: ")
computer=random.choice(['r','p','s'])
print('Your Choice:',a,'Computer Choice:',computer)

if a==computer:
    print("Tie")
    
elif a=='r' and computer=='p' :
    print('computer Wins, You lost!')
elif a=='r' and computer=='s':
    print('You Wins!!!')
elif a=='p' and computer=='s':
    print('computer Wins, You lost!')
elif a=='p' and computer=='r':
    print('You wins!!!')
elif a=='s' and computer=='r':
    print('computer Wins, You lost!')
elif a=='s' and computer=='p':
    print('You Wins!!!')
else:
    print('Invalid')
'''

''' The main difference is that here i'm using or function for multiple cases and no other changes i made in the game 

import random

name=input('Enter your name:')
print('Welcome',name,'\N{Grinning Face}',' to the RPS game!!!')
print('Enter your choice')
a=input("'r' for rock, 'p' for paper, 's' for scissors: ")
computer=random.choice(['r','p','s'])
print('Your Choice:',a,'Computer Choice:',computer)

if a==computer:
    print("Tie")
    
elif (a=='r' and computer=='p') or (a=='p' and computer=='s') or (a=='s' and computer=='r'):
    print('computer Wins, You lost!')
    
elif (a=='r' and computer=='s') or (a=='p' and computer=='r') or (a=='s' and computer=='p'):
    print('You Wins!!!')

else:
    print('Invalid')
    
'''