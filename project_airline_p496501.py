#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:06:05 2026

@author: xuzikang
"""
# reference the random, string, sqlite3
import random
import sqlite3

# create the dictionary of seats
rows = 80
column = ["A","B","C","D","E","F"]
seats = {}

# make a range from rows and columns, which limit the range of seats that customers can choose
for r in range(1, rows+1):
    for c in column:
        seats[str(r)+c] = "Free"

# store the refferences that have been used
used_references = []

# connect the database
conn = sqlite3.connect("/Users/xuzikang/Desktop/booking.db")
cursor = conn.cursor()

# create table if table does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    reference TEXT PRIMARY KEY,
    passport TEXT,
    first_name TEXT,
    last_name TEXT,
    seat TEXT
)
""")
conn.commit()

# the code about create the unique booking references of each customers
def get_references():
    words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    words_number = words + numbers
    
    while True:
        references = ""
        for i in range(8):
            references += random.choice(words_number)
        if references not in used_references:
            used_references.append(references)
            break
    
    return references

# check seats
def check_seat():
    seat = input("Enter seat number: ")
    if seat in seats:
        if seats[seat] == "Free":
            print("This seat is free")
        else:
            print("This seat is already booked")
    else:
        print("Wrong seat number")
    
# book seats        
def book_seat():
    seat = input("Enter seat number: ")

    if seat in seats:
        if seats[seat] == "Free":
# get customer information
            passport = input("Passport: ")
            first = input("First name: ")
            last = input("Last name: ")
# create booking references
            references = get_references()
# update seat status
            seats[seat] = references
# save into database
            cursor.execute(
                "INSERT INTO bookings VALUES (?, ?, ?, ?, ?)",
                (references, passport, first, last, seat)
            )
            conn.commit()

            print("you booked successfully")
            print("Reference:", references)

        else:
            print("Seat have been booked")
    else:
        print("Invalid seat")

# cancel booking        
def free_seat():
    seat = input("Enter seat number: ")

    if seat in seats:
        if seats[seat] != "Free":

            references = seats[seat]

# delete from database
            cursor.execute("DELETE FROM bookings WHERE reference = ?", (references,))
            conn.commit()
# reset seats
            seats[seat] = "Free"
            print("Booking cancelled")

        else:
            print("Tseat is free")
    else:
        print("Inumber is wrong")

# show all seats
def show_status():
    for seat, status in seats.items():
        print(seat, status)

# show free seats' number
def show_number_of_free_seats():
    count = list(seats.values()).count("Free")
    print("number of free seats:", count)

# cycle operation, and create the menu        
while True:
    print("choose aseat system")
    print("1.check seat")
    print("2.book seat")
    print("3.free seat")
    print("4.show seat status")
    print("5.exit")
    print("6.show free seats")

# define each number in the menu
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
        
    

