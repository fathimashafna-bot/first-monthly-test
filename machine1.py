def book_room(bookings):
    room_no = input("Enter Room Number: ")
    if room_no in bookings:
        print("Room Number is already booked.")
    guest_name = input("Enter Guest Name: ")
    room_type = input("Enter Room Type: ")
    days = int(input("Enter Number of Days: "))
    while days <= 0:
        print("Number of Days should be greater than 0.")
        days = int(input("Enter Number of Days: "))
    price = float(input("Enter Total Price: "))
    while price <= 0:
        print("Total Price should be greater than 0.")
        price = float(input("Enter Total Price: "))
    bookings[room_no] = {
        "Guest Name": guest_name,
        "Room Type": room_type,
        "Days": days,
        "Total Price": price
    }
    print("Room Booked Successfully.")


def view_bookings(bookings):
    if len(bookings) == 0:
        print("No Booking Records Found.")
        return
    for room_no in bookings:
        print("Room Number:", room_no)
        print("Guest Name:", bookings[room_no]["Guest Name"])
        print("Room Type:", bookings[room_no]["Room Type"])
        print("Number of Days:", bookings[room_no]["Days"])
        print("Total Price:", bookings[room_no]["Total Price"])
def search_booking(bookings):
    room_no = input("Enter Room Number: ")

    if room_no in bookings:
        print("Room Number:", room_no)
        print("Guest Name:", bookings[room_no]["Guest Name"])
        print("Room Type:", bookings[room_no]["Room Type"])
        print("Number of Days:", bookings[room_no]["Days"])
        print("Total Price:", bookings[room_no]["Total Price"])
    else:
        print("Booking Not Found.")
def update_days(bookings):
    room_no = input("Enter Room Number: ")

    if room_no in bookings:
        days = int(input("Enter New Number of Days: "))

        while days <= 0:
            print("Number of Days should be greater than 0.")
            days = int(input("Enter New Number of Days: "))

        bookings[room_no]["Days"] = days

        print("Booking Days Updated Successfully.")
    else:
        print("Booking Not Found.")
def cancel_booking(bookings):
    room_no = input("Enter Room Number: ")

    if room_no in bookings:
        del bookings[room_no]
        print("Booking Cancelled Successfully.")
    else:
        print("Booking Not Found.")



bookings = {}

while True:
    print("\nHotel Room Booking System")
    print("1. Book Room")
    print("2. View All Bookings")
    print("3. Search Booking")
    print("4. Update Booking Days")
    print("5. Cancel Booking")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_room(bookings)

    elif choice == 2:
        view_bookings(bookings)

    elif choice == 3:
        search_booking(bookings)

    elif choice == 4:
        update_days(bookings)

    elif choice == 5:
        cancel_booking(bookings)

    elif choice == 6:
        print("Thank You... Program Terminated.")
        break

    else:
        print("Invalid Choice. Please try again.")