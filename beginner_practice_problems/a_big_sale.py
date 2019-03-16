# CodeChef          : https://www.codechef.com/users/kodeutility
# GitHub            : https://www.github.com/kodeutility
# Portfolio website : https://kodeutility.github.io/
# Author            : Kiran BG
# Question link     : https://www.codechef.com/problems/BIGSALE

# cook your dish here
for _ in range(int(input())):
    recipe_types = int(input())
    total_loss = 0
    for _ in range(recipe_types):
        price, quantity, discount = map(int,input().split())
        new_price = price + (price * (discount/100))
        price_after_discount = new_price - (new_price * (discount/100))
        loss = quantity * (price - price_after_discount)
        total_loss += loss
    print(total_loss)    
