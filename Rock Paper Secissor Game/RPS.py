import random

print("🎮 Welcome to Rock, Paper, Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.\n")

while True:
    user_input = input("Your move: ").lower()
    if user_input == 'quit':
        print("Thanks for playing! Goodbye 👋")
        break

    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input! Please choose rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!\n")
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'paper' and computer_choice == 'rock') or \
         (user_input == 'scissors' and computer_choice == 'paper'):
        print("🎉 You win!\n")
    else:
        print("😢 You lose!\n")
