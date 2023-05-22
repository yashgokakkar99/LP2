import csv
import time

def create_inquiry():
    name=input("Enter our name : ")
    age=int(input("Enter your age : "))
    city=input("Enter your city : ")
    inquiry=input("Enter your inquiry : ")

    with open("medical_expert.csv",'a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([name, age, city, inquiry])
    
    print("Inquiry submitted successfully !")
    print("Thank you for contacting us !!")

    print("Your inquiry is being analyzed by our experts....")
    time.sleep(5)
    if(age>=18):
        print("Based on your and your inquiry we recommend you to take covid19 vaccine immediately.")
    else:
        print("Based on your inquiry and age, it is recommended to consult with a healthcare professional regarding COVID-19 vaccination eligibility.")

def view_enquiries():
    with open("medical_expert.csv",'r') as file:
        reader=csv.reader(file)
        for row in reader:
            name,age,city,inquiry=row
            print(f"\nName: {name}")
            print(f"Age: {age}")
            print(f"City: {city}")
            print(f"Inquiry: {inquiry}")

while True:
    print("Medical and Hospital management expert system : ")
    print("Menu : ")
    print("1. Submit an inquiry")
    print("2. View inquiries")
    print("3. Exit")

    choice = int(input("Enter your choice (1,2, or 3): "))
    if choice==1:
        create_inquiry()
    elif choice==2:
        view_enquiries()
    elif choice==3:
        print("Exiting....")
        time.sleep(3)
        break
    else:
        print("Oops!! Error")
        
