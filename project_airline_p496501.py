#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:06:05 2026

@author: xuzikang
"""


rows = 80
column = ["A","B","C","D","E","F"]
seats = {}

for r in range(1, rows+1):
    for c in column:
        seats[str(r)+c] = "Free"
 
def check_seat():
    seat = input("please enter the seat number: ")
    if seat in seats:
        if seats[seat] == "Free":
            print("It is free seat")
        else:
            print("seat is booked")
    else:
        print("number is wrong")
        
def book_seat():
    seat = input("please enter the seat number: ")
    if seat in seats:
        if seats[seat] == "Free":
            print("It has booked successfully")
        else:
            print("It has been booked")
    else:
        print("number is wrong")
        
def free_seat():
    seat = input("please enter the seat number: ")
    if seat in seats:
        if seats[seat] != "Free":
            print("free it successfully")
        else:
            print("It idon't need free")
    else:
        print("number is wrong")
        
def show_status():
    for seat, status in seats.items():
        print(seat, status)
        
def show_number_of_free_seats():
    count = list(seats.values()).count("Free")
    print("number of free seats:", count)
        
while True:
    print("choose aseat system")
    print("1.check seat")
    print("2.book seat")
    print("3.free seat")
    print("4.show seat status")
    print("5.exit")
    print("6.show free seats")
    
    choice = input("choose a number: ")
    if choice == "1":
        check_seat()
    elif choice == "2":
        book_seat()
    elif choice == "3":
        free_seat()
    elif choice == "4":
        show_status()
    elif choice == "5":
        break
    elif choice == "6":
        show_number_of_free_seats()
    else:
        print("Wrong input")
        
    

