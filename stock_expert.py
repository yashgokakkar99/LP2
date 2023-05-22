import csv

def analyze(symbol):
    if symbol=="AWL":
        return "Buy"
    elif symbol=="LIC":
        return "Sell"
    else:
        return "Hold"

def process_input(stock_symbol):
    recommendation = analyze(stock_symbol)
    with open("Stock_expert.csv",'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([stock_symbol,recommendation])

def view_recom():
    with open("Stock_expert.csv",'r') as file:
        reader = csv.reader(file)
        for row in reader:
            stock_symbol, recommendation=row
            print(f"Stock : {stock_symbol}")
            print(f"Recommendation : {recommendation}")

while True:
    print("Welcome to stock expert !!")
    print("Menu : ")
    print("1. Analyze stock")
    print("2. View recommendations")
    print("3. Exit")

    choice=int(input("Enter any choice from(1,2 and 3) : "))

    if(choice==1):
        stock_symbol=input("Enter stock symbol : ")
        process_input(stock_symbol)
    elif choice==2:
        view_recom()
    elif choice==3:
        print("exiting...")
        break
    else:
        print("Error")

