# Build flashcard using class in Python.
# Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization.
#  Flashcards usually have a question on one side and an answer on the other.
# Example 1:
# Approach:
# Create a class named FlashCard.
# Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. 
# E.g., {"Banana": "yellow", "Strawberries": "pink"}
# Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
# Now prompt the user to answer the color of the randomly chosen fruit.
# If correct print correct else print wrong.

# Output:
# welcome to fruit quiz
# What is the color of Strawberries
# pink
# Correct answer
# Enter 0, if you want to play again: 0
# What is the color of watermelon
# green
# Correct answer
# Enter 0, if you want to play again: 1



import random

class FlashCard:

    def __init__(self):
        self.fruits = {"Banana": "yellow", "Strawberries": "pink", "Watermelon": "green"}
        print("welcome to fruit quiz")

    def play(self):
        fruit, color = random.choice(list(self.fruits.items()))
        print("What is the color of", fruit)
        ans = input()
        if ans == color:
            print("Correct answer")
            print("Enter 0, if you want to play again: ")
            if input() == "0":
                self.play()
        else:
            print("Wrong answer")
            print("Enter 0, if you want to play again: ")
            if input() == "0":
                self.play()
        return
    

obj = FlashCard()
obj.play()