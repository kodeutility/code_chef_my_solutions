# CodeChef          : https://www.codechef.com/users/kodeutility
# GitHub            : https://www.github.com/kodeutility
# Portfolio website : https://kodeutility.github.io/
# Author            : Kiran BG
#Question link      : https://www.codechef.com/problems/HS08TEST

if __name__ == '__main__':
    withdrawal_amount, balance = (map(float,input().split()))

    if (withdrawal_amount > (balance-0.5)):
        print(balance)
    elif withdrawal_amount%5 != 0:
        print(balance)
    else :
        print(balance-withdrawal_amount-0.5)
