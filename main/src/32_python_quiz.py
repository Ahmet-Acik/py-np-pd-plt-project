"""
Python Quiz: Test Your Knowledge

A simple interactive quiz on Python basics.
Run this script to answer questions.
"""

def ask_question(question, options, correct_index):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Your answer (number): "))
            if 1 <= answer <= len(options):
                return answer - 1 == correct_index
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def main():
    questions = [
        {
            "question": "What is the output of print(2 + 3)?",
            "options": ["5", "23", "Error", "None"],
            "correct": 0
        },
        {
            "question": "Which data type is immutable in Python?",
            "options": ["List", "Dictionary", "Tuple", "Set"],
            "correct": 2
        },
        {
            "question": "How do you start a function definition?",
            "options": ["func", "def", "function", "start"],
            "correct": 1
        }
    ]

    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['options'][q['correct']]}\n")

    print(f"Your score: {score}/{len(questions)}")
    if score == len(questions):
        print("Perfect! You're a Python expert.")
    elif score > len(questions) // 2:
        print("Good job!")
    else:
        print("Keep practicing!")

if __name__ == "__main__":
    main()