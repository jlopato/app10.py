# Building a QCM :
import Question from Question
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
