# To generate the quiz questions

questions = [
    {"Question": "1.Which country hosted the Summer Olympics in 2024?",
     "Options": "A. Japan\nB. France\nC. USA\nD. Australia\n",
     "Answer": "B"},
    
    {"Question": "2.Who is known as the father of modern physics?",
     "Options": "A. Isaac Newton\nB. Albert Einstein\nC. Nikola Tesla\nD. Galileo Galilei\n",
     "Answer": "B"},
    
    {"Question": "3.What is the capital city of Japan?",
     "Options": "A. Seoul\nB. Beijing\nC. Tokyo\nD. Bangkok\n",
     "Answer": "C"},
    
    {"Question": "4.Which planet is known as the Red Planet?",
     "Options": "A. Mars\nB. Earth\nC. Venus\nD. Jupiter\n",
     "Answer": "A"},
    
    {"Question": "5.What is the largest ocean on Earth?",
     "Options": "A. Atlantic Ocean\nB. Indian Ocean\nC. Arctic Ocean\nD. Pacific Ocean\n",
     "Answer": "D"}
]

def run_quiz(questions):
    score = 0
    for question in questions:
        while True: 
            print(question["Question"])
            print(question["Options"])
            answer = input("Enter your answer (A,B,C,D)\n").upper()
            
            if answer in ['A', 'B', 'C', 'D']: 
                if answer == question["Answer"]:
                    print("Hurray! You entered the correct option.\n")
                    score += 1
                else:
                    print(f"You entered the wrong option {answer}.")
                    print(f"Correct option is {question['Answer']}\n")
                break  
            else:
                print("Please enter a valid option (A, B, C, or D).\n")
    
    return score

def main():
    val = run_quiz(questions)
    print(f"Your Score is {val}")

if __name__ == '__main__':
    main()
