print("Welcome to the Movie Ticket Booking Calculator!")
base_price = 15
age = int(input("Enter your age"))
seat_type = "Gold"
show_time = "Evening"

if age > 17:
    print("User is eligible to book a ticket")

if age >= 21:
    print("User is eligible for Evening shows")
else:
    print('User is not eligible for Evening shows')

is_member = False # True to get discount
is_weekend = False

discount = 0
# using and statement makes sure every aguments is correct to executes
if is_member and age >= 21:
    discount = 3  # updating the discount
    print("User qualifies for membership discount")
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)  # shows the updated value of discount if is_member is True

extra_charges = 0
# using or statement makes sure one is correct to executes
if is_weekend or show_time == "Evening":  # if there is a weekend it leads to extra charges
    extra_charges = 2
    print("Extra charges will be applied")
else:
    print("No extra charges will be applied")
print("Extra charges:",extra_charges)  #updates the variable of extra charge if its weekend

# if show is not in evening and age is above 17 then also eligible
# if we use multiple operand then we can use ()to separate them, so before it going to "and" it checks the "or" statement
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
    service_charges = 0  #if we don't use indentation before else statement that raises syntax error
    if seat_type == "Premium":  #its called nested statement after out if true then it comes to inner if
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1
    print("Service charges:", service_charges)
    final_price = base_price + extra_charges + service_charges
    final_price -= discount
    print("Final price of a ticket:", final_price)
else:
    print('Ticket booking failed due to restrictions')