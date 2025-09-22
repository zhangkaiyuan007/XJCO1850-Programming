# Welcome the user to the quiz program
# Explain that they will answer multiple-choice questions
print("Welcome to the Quiz!")
print("You will answer multiple-choice questions.\n")
# Initialize a score counter to keep track of correct answers
score = 0
# Present the first question
# Display the question text and the multiple-choice answers
# you can think of questions yourself, or find them online
quiz = [
  {
    "question": "What is the capital of France?",
    "options": ["a) Berlin", "b) Paris", "c) Madrid", "d) Rome"],
    "answer": "b"
  },
  {
    "question": "Which language is primarily used for web development?",
    "options": ["a) Python", "b) C++", "c) JavaScript", "d) Java"],
    "answer": "c"
  },
  {
    "question": "What does CPU stand for?",
    "options": ["a) Central Processing Unit", "b) Computer Power Unit", "c) Central Programming Unit", "d) Control Processing Unit"],
    "answer": "a"
  }
]
# Get the user's input for their answer to the first question

# Check if the answer is correct
# If the answer is correct, print a success message and increase the score
# If the answer is incorrect, print the correct answer

# Repeat the above steps for additional questions (Question 2, Question 3, etc.)
for q in quiz:
  print(q["question"])
  for opt in q["options"]:
    print(opt)
  user_answer = input("Enter your answer (a/b/c/d): ").strip().lower()
  
  if user_answer == q["answer"]:
    print("Correct!\n")
    score += 1
  else:
    print(f"Incorrect. The correct answer is '{q['answer']}'.\n")
# After all questions are answered, display the final score to the user
# Thank them for participating in the quiz
print(f"Quiz finished! Your final score is: {score}/{len(quiz)}")
print("Thank you for participating!")
###### Extensions ######

# Use a loop to let people re-try the quiz
# create a leaderboard which stores users with the highest score
# Create a menu to let people access the leaderboard or the quiz
# Modularise the code to make it shorter and more maintainable