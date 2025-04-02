# Created by DragonNoir_off
# link to GitHub profile : https://github.com/DragonNoir-off
# Last edit -> 02/04/2025
# version [ 1 ]

def fib(n1 : int, n2 : int, loop : int, deep : int):
    n3 = n1 + n2
    if loop == deep: return n3
    loop = loop + 1
    return fib(n2, n3, loop, deep)

nb = int(input("entrer le nombre de fib(x) a calculer ( max 998 ), x = "))
print(fib(0, 1, 0, nb))
