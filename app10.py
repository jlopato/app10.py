# Building a QCM :
from Question import Question
question_prompts = [
    "What is the color of apple? \na- Red\nb- White\nc- Black\n\n",
    "What is the color of banana? \na- Red\nb- White\nc- Black\n\n",
    "What is the color of strawberry? \na- Red\nb- White\nc- Black\n\n",
]
question = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"a"),
]
def run_test(question):
    score = 0
    for question in question:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("you got" + str(score)+ "/" + str(len(questions))+ "correct")

run_test(question)