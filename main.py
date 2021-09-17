from random import randint

# The dictionary to the 3 possible answers
answers = {1 : "Yes", 2 : "No", 3 : "I don't know"}

# Main loop to read the "inputs"
def main():
    run = 1
    while run == 1:
        the_input = input(">> ")
        if the_input != "quit":
            answerGenerator()
        else:
            run = 0

# Generate an answer
def answerGenerator():
    possibility = randint(1, 3)
    print(answers[possibility])

main()
