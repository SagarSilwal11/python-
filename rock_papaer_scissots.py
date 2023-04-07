import random

print("Welcome to game zone!Here we present scissors,papper and rock game")
Computer_wins=0
You_win=0
options=["scissors","paper","rock"]
name=input("Enter your name!\n").upper()
while True:
    
    user_input=input(f'{name}!Enter scissors,paper,rock or quit (q)\n').lower()
    print(f'{name} enter {user_input}.')
    if user_input=='q':
        break
    if user_input not in options:
            continue
    random_number=random.randint(0,2)
    computer_input=options[random_number]
    print(f'Computer enter {computer_input}.')
    
    if user_input=="scissors" and computer_input=='paper':
        print("You win")
        You_win+=1
    elif user_input=="paper" and computer_input=='rock':
        print("You win")
        You_win+=1
    elif user_input=="rock" and computer_input=='scissors':
        print("You win")
        You_win+=1
    else:
        print("Computer Wins!")
        Computer_wins+=1


print(f"{name} wins=",You_win)
print("Computer wins=",Computer_wins)
