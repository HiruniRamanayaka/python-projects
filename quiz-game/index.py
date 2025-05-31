# create an object with questions

questions = [
    {
        "prompt": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Mars"],
        "answer": "C"
    },
    {
        "prompt": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "What is the freezing point of water in Celsius?",
        "options": ["A. 0°C", "B. 32°C", "C. -10°C", "D. 100°C"],
        "answer": "A"
    },
    {
        "prompt": "What is the chemical symbol for gold?",
        "options": ["A. Ag", "B. Au", "C. Hg", "D. Pb"],
        "answer": "B"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)

        # get user's answer
        answer = input("Enter your answer (A, B, C, D): ").upper()
        
        if answer == question["answer"]:
            print("Correct!\n")
            score+=1
        else:
            print("Incorrect. The correct answer is " + question["answer"] + "\n")
            # print(f"Incorrect. The correct answer is {question['answer']}.\n")

    # print final score
    print(f"You got {score} out of {len(questions)} questions correct.\n")

run_quiz(questions)