from Question import Question

question_prompts = [
    "What age is Wayne?\n(a) 23\n(b) 22\n(c) 21\n\n",
    "What age is Alpha?\n(a) 13\n(b) 14\n(c) 15\n\n",
    "What age is Judah?\n(a) 20\n(b) 18\n(c) 19\n\n",
    "What age is Mj?\n(a) 27\n(b) 26\n(c) 28\n\n",
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " questions right!")

run_test(questions)
