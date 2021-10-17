import math_pi

def find_pi_to_the_nth_digit():
    pi = math_pi.pi()

    nth_digit = int(input('enter nth digit for PI:'))
    print(pi[:nth_digit+2])

find_pi_to_the_nth_digit()