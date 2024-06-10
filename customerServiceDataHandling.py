#Task 1: Customer Service Ticket Tracker
#Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
#Problem Statement:
#Develop a program that:
#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.
#Initialize with some sample tickets and include functionality for additional ticket entry.
#Example ticket structure:
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(service_tickets):
    ticket_num = "Ticket{:03d}".format(len(service_tickets) + 1)
    customer = input("Enter customer name.: ")
    issue = input("Enter issue description.: ")
    status = "open"

    service_tickets[ticket_num] = {"Customer": customer, "Issue": issue, "Status": status}
    print("New ticket added successfully!")
    return service_tickets

def update_ticket(service_tickets):
    ticket_num = input("Which ticket would you like to update? (examle: Ticket001): ").capitalize()
    if ticket_num not in service_tickets:
        print("Ticket number not found.")
        return service_tickets
    
    print("Current ticket details:")
    print(service_tickets[ticket_num])

    update_field = input("Enter the field to update (Customer / Issue / Status): ").capitalize()
    if update_field not in ["Customer", "Issue", "Status"]:
        print("Invalid field.")
    new_value = input(f"Enter the new value for {update_field}: ")
    service_tickets[ticket_num][update_field] = new_value

    print("Ticket updated successfully!")
    return service_tickets



def display_tickets():
    for ticket, info in service_tickets.items():
        customer = info["Customer"]
        issue = info["Issue"]
        status = info["Status"]
        print(f"Ticket: {ticket}, Customer: {customer}, Issue: {issue}, Status: {status}")


while True:
    print("Menu:")
    print("1. Open New Ticket")
    print("2. Update Ticket Status")
    print("3. Display All Tickets")
    print("4. Quit")

    action = input("Select what action you'd like to perform: ")

    if action == '1':
        add_ticket(service_tickets)
    elif action == '2':
        update_ticket(service_tickets)
    elif action == '3':
        display_tickets()
    elif action == '4':
        break
    else:
        print("Please input a valid entry.")
