my_file = open('questions.txt', 'r')
questions_answers = [line.strip() for line in my_file.readlines()]
my_file.close()

questions = []
answers = []

for line in questions_answers:
  question_answer = line.split('=')
  questions.append(question_answer[0]+"=")
  answers.append(question_answer[1])


correct_responses = 0
maximum_score = len(questions)

for count, question in enumerate(questions):
  user_input = input(f"Question {count + 1}: {question}").strip()
  if user_input == answers[count]:
    correct_responses += 1
  
results_file = open('result.txt', 'w')
results_file.write(f"Your final score is {correct_responses}/{maximum_score}.")
results_file.close()
