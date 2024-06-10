#Task 1: Hotel Room Booking Tracker
#Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.
#Problem Statement:
#Develop a program that:
#Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
#Implement functions to:
#Book a room (mark as booked and assign to a customer).
#Check-out a customer (mark room as available and remove customer name).
#Display the status of all rooms.
#Start with this initial hotel room structure:
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}
def book_room():
    customer_name = input("Enter the name of the customer: ")
    room_number = input("Which room is being booked?: ")
    if room_number in hotel_rooms:
        if hotel_rooms[room_number] ["status"] == "available":
            hotel_rooms[room_number] ["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} has been booked by {customer_name}")
        else:
            print(f"{room_number} is already booked.")
    else:
        print(f"Room {room_number} does not exist.")

def check_out():
    room_number = input("Which room is checking out?: ")
    if room_number in hotel_rooms:
        if hotel_rooms[room_number] ["status"] == "booked":
            hotel_rooms[room_number] ["status"] = "available"
            hotel_rooms[room_number] ["customer"] = ""
            print(f"Room {room_number} has checked out.")
        else:
            print(f"Room {room_number} does not have anybody checked in.")
    else:
        print("Please input a valid room number.")

def print_room_info():
    for room_number, info in hotel_rooms.items():
        status = info["status"]
        customer = info["customer"]
        print(f"Room: {room_number}, Status: {status}, Customer: {customer}")


while True:
    print("Menu:")
    print("1. Book a Room")
    print("2. Check Out Customer")
    print("3. Rooms Status")
    print("4. Quit")
    
    option = input("Enter the number for the task you'd like to do: ")
    
    if option == '1':
        book_room()        
    elif option == '2':
        check_out()
    elif option == '3':
        print_room_info()
    elif option == '4':
        break
    else:
        print("Please enter a number next to the action you'd like to perform.")