questions =("Who wrote Pride and Prejudice?",
            "What is the name of the wizarding school in Harry Potter?",
            "Which novel begins with the line Call me Ishmael?",
            "Who is the author of The Great Gatsby?",
            "Who wrote the epic poem Paradise Lost?")

options=(("A. Charlotte Bronte","B. Jane Austen ","C. Franz Kafka ","D. Emily Dickinson"),
         ("A. Ilvermorny","B. Hogwarts","C. Harmony","D. Beauxbatons"),
         ("A. Moby-Dick","B. The Old Man and The Sea","C. Heart of Darkness","D. Robinson Crusoe"),
         ("A. F. Scott Fitzgerald","B. Ernest Hemingway","C. William Shakespeare","D. William Faulkner"),
         ("A. John Donne","B. John Milton","C. Geoffrey Chaucer","D. William Blake"))

answers=("B", "B", "A", "A", "B")

guesses=[]

score=0

question_num=0

for question in questions:
    print("-----------------------------------------")
    print(question)
    
    for option in options[question_num]:
        print(option)


    guess=input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")        
    question_num += 1



print("-----------------------------------------")
print("                 RESULT                  ")
print("-----------------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()   

score_percentage= int((score/len(questions))*100)

print(f"Your score is: {score_percentage}%")


