import csv
def employee_eval():
    print("Welcome to employee evaluation system !!")

    while True:
        print("Menu : ")
        print("1. Evaluate employee performance")
        print("2. Exit")

        choice = int(input("Enter a choice (1 or 2) : "))

        if(choice==1):

            id=input("Enter employee id :")
            name=input("Enter employee name : ")
            att_score=float(input("Enter employee attendance score (out of 100): "))
            sal_score=float(input("Enter employe salses score (out of 100): "))

            overall_score = (att_score+sal_score)/2

            if(overall_score>=90):
                rating="Excellent"
            elif(overall_score>=80):
                rating="Very Good"
            elif(overall_score>=70):
                rating="Good"
            else:
                rating="Bad"
            
            print(f"Mr/Mrs {name} your employee rating is ",rating)
            with open("employee_evaluation.csv",'a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([id,name,att_score,sal_score,rating])
        elif(choice==2):
            print("Exiting....")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
employee_eval()
