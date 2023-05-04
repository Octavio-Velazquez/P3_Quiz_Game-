# Quiz Game!

# Create a dictionary nested with the number of the question in the first dictionary
# and the question and answer in the second dictionary.
quiz = {
    "Question 1": {
        "question": "What is the capital of Dominican Republic?",
        "answer": "Santo Domingo"
    },
    "Question 2": {
        "question": "What is the capital of Equator?",
        "answer": "Quito"
    },
    "Question 3": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "Question 4": {
        "question": "What is the capital of Argentina?",
        "answer": "Buenos Aires"
    },
    "Question 5": {
        "question": "What is the capital of Cuba?",
        "answer": "La Habana"
    },
    "Question 6": {
        "question": "What is the capital of USA?",
        "answer": "Washington"
    },
    "Question 7": {
        "question": "What is the capital of Canada?",
        "answer": "Ottawa"
    },
    "Question 8": {
        "question": "What is the capital of Venezuela?",
        "answer": "Caracas"
    },
}

# Counter with the score of the questions
score = 0

for key, value in quiz.items():
    print(key + ": " + value["question"])
    answer = input("Answer?: ")

    if answer.title() == value["answer"].title():
        print("Correct!\n")
        score += 1  # score = score + 1

    else:
        print("Wrong!")
        print("The answer is: " + value["answer"])
        print("\n")

if score >= 4:
    print(f"Your total score is: {score} correct answers!")
    print("Well done!")
elif score <= 1:
    print(f"Your total score is: {score} correct answer!")
    print("You have to start studying geography immediately!")
else:
    print(f"Your total score is: {score} correct answers!")
    print("You have to start studying geography!")

