import random

def game(comp, you):
    if comp == you:
        return 0  # Tie
    
    elif (comp == 's' and you == 'w') or \
         (comp == 'w' and you == 'g') or \
         (comp == 'g' and you == 's'):
        return -1  # Computer wins
    
    return 1  # You win

def snake_water_gun():
    choice = {
        's': 'Snake',
        'w': 'Water',
        'g': 'Gun'
    }
    
    comp = random.choice(list(choice.keys())) 
    you = input("Enter your choice: Snake(s), Water(w), Gun(g): ").strip().lower()

    if you not in choice:
        print("Invalid choice! Please choose 's', 'w', or 'g'.")
        return

    print(f"You chose {choice[you]}")
    print(f"Computer chose {choice[comp]}")
    
    result = game(comp, you)
    
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You win!")
    else:
        print("You lose!")
    

if __name__ == "__main__":
    snake_water_gun()
