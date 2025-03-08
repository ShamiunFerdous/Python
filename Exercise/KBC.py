ques = [
    ["What is the capital of France?", ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "C"],
      
    ["Who is the author of 'Harry Potter' series?", ["A. J.K. Rowling", "B. J.R.R. Tolkien", "C. Dan Brown", "D. Agatha Christie"], "A"],
    
    ["Who wrote 'Hamlet'?", ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"], "B"]
]

prize_money = [1000, 5000, 10000]
total_earnings = 0

print("Welcome to KBC!")

for i in ques:
    print(i[0])
    for j in i[1]:
        print(j)
        
    ans = input("Enter your answer: ")
    
    if ans.strip().upper() == i[2]:
        print("Correct!")
        total_earnings += prize_money[ques.index(i)]
        
    else:
        print("Incorrect!")
        break
    
print("Congratulations! You have won", total_earnings)
    