"""Prime Number:
Have the user enter a number, find Prime Number next to it and diplay."""

def prime_finder():
    input_number = int(input("Type number:"))
    number_to_check = input_number + 1
    while True:
        if number_to_check % 2 != 0:
            print("Prime number next to unput: ", input_number, " is: ", number_to_check)
            return False, "Prime number next to unput: ", str(input_number), " is: ", str(number_to_check)
        else:
            number_to_check += 1

prime_finder()