"""
Ticket Booking System
Create a menu:

Book Ticket
Cancel Ticket
View Available Seats
Exit

Rules:

Total seats = 50
Booking cannot exceed available seats.
Cancellation cannot make booked seats negative.
Keep showing the menu until the user chooses Exit.
"""
import random
def book_ticket(seats,confirm_seats):
    name=input("enter your name : ")
    if len(seats)==0:
        print("ther are no avilable seats ")
    elif name in confirm_seats:
        print("You already have a booked ticket.")
    else:
        seat_available=random.choice(seats) 
        seats.remove(seat_available)
        confirm_seats[name]=seat_available
        print(f" {name} : {seat_available}")
    return seats,confirm_seats

def cancel_ticket(seats,confirm_seats):
    name=input("enter your name : ")
    if name in confirm_seats:
        ticket_num=int(input("enter your ticket number : "))
        if confirm_seats[name]==ticket_num:
            confirm_seats.pop(name)
            seats.append(ticket_num)
            seats.sort()
        else:
            print("sorry ! this is not your ticket number")
            print("try again")
    else:
        print("sorry ! this is not your ticket number")
        print("try again")

    return seats,confirm_seats
    
def view_available_seats(seats):
    return seats

def exit_program():
    return "thank you for vist"
       
seats = list(range(1, 51))
confirm_seats={}
while True:
    print("click 1 for booking ")
    print("click 2 for cancel ")
    print("click 3 check availablity")
    print("click 4 for exit")
    choice=int(input("enter your choice"))
    if choice==4:
        print(exit_program())
        break
    elif choice==1:
        seats,confirm_seats=book_ticket(seats,confirm_seats)
    elif choice==2:
        seats,confirm_seats=cancel_ticket(seats,confirm_seats)
    elif choice==3:
        print("Available seats:", view_available_seats(seats))
    else:
        print("invalid option")


    
