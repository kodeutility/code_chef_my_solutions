# CodeChef          : https://www.codechef.com/users/kodeutility
# GitHub            : https://www.github.com/kodeutility
# Portfolio website : https://kodeutility.github.io/
# Author            : Kiran BG
# Question link     : https://www.codechef.com/problems/FLOW018

for _ in range(int(input())):
    number = int(input())
    def fact(number):
        if number==1:
            return 1
        else:
            return number * fact(number-1)
    print(fact(number))
