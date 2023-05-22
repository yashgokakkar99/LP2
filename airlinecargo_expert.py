import csv
import time

def sch_flight(flight_details):
    sch = "Flight Scheduled Successfully"
    print("loading...")
    time.sleep(2)
    return sch

def sch_cargo(cargo_details):
    sch = "Cargo Scheduled Successfully"
    print("loading...")
    time.sleep(2)
    return sch

def add_flight():
    flight_number = input("Enter the flight number: ")
    departure_city = input("Enter the departure city: ")
    destination_city = input("Enter the destination city: ")
    departure_time = input("Enter the departure time: ")
    arrival_time = input("Enter the arrival time: ")

    flight_details={
        "flight_number": flight_number,
        "departure_city": departure_city,
        "destination_city": destination_city,
        "departure_time": departure_time,
        "arrival_time": arrival_time
    }

    schedule = sch_flight(flight_details)

    with open('airline_schedule.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([flight_number, departure_city, destination_city, departure_time, arrival_time, schedule])
    print("Updating....")
    time.sleep(3)

    print("Flight schedule added successfully!")

def add_cargo():
    shipment_id = input("Enter the shipment ID: ")
    origin = input("Enter the origin: ")
    destination = input("Enter the destination: ")
    departure_date = input("Enter the departure date: ")
    arrival_date = input("Enter the arrival date: ")

    shipment_details = {
        "shipment_id": shipment_id,
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date,
        "arrival_date": arrival_date
    }

    schedule = sch_cargo(shipment_details)

    with open('cargo_schedule.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([shipment_id, origin, destination, departure_date, arrival_date, schedule])
    print("Updating....")
    time.sleep(3)
    print("Cargo schedule added successfully!")

def view_flight_schedules():
    with open('airline_schedule.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))

def view_cargo_schedules():
    with open('cargo_schedule.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))
print("Welcome to the Airline and Cargo Scheduling Expert System!")
while True:
    print("\nMenu:")
    print("1. Add flight schedule")
    print("2. Add cargo schedule")
    print("3. View flight schedules")
    print("4. View cargo schedules")
    print("5. Exit")

    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    if choice == "1":
        add_flight()

    elif choice == "2":
        add_cargo()

    elif choice == "3":
        view_flight_schedules()

    elif choice == "4":
        view_cargo_schedules()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
