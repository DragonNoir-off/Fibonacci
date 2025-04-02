# Created by DragonNoir_off
# link to GitHub profile : https://github.com/DragonNoir-off
# Last edit -> 02/04/2025
# version [ 1 ]

import time
import math

def fib(n : int):
    if n<0: return False
    def f(n1 : int, n2 : int):
        n3 = n1 + n2
        return n2, n3

    n1, n2 = 0, 1

    while n>0:
        n = n -1
        n1, n2 = f(n1, n2)
    return True, n2

def test_fib(number_actual, see_last_number):
    temps_debut = time.monotonic()
    result, number = fib(number_actual)
    if result == False:
        print("Failed")
    temps_fin = time.monotonic()

    delta_temps = math.ceil((temps_fin-temps_debut)*10**8)/10**8
    print("fib("+str(number_actual)+") -- "+str(delta_temps))
    if see_last_number: print(number)

def start_test():
    max_number = 1000000
    number_actual = 10
    while max_number > number_actual:
        number_actual = number_actual * 10
        test_fib(number_actual, False)

    print("test ended")

    num = int(input("input a number 'n' to see the work time of fib(n) function -> "))
    test_fib(num, True)

start_test()
