from Question import Question

question_prompts = [
    "What age is Wayne?\n(a) 23\n(b) 22\n(c) 21\n\n"
    "What age is Alpha?\n(a) 13\n(b) 14\n(c) 15\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)