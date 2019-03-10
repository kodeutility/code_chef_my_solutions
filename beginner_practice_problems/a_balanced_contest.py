# CodeChef          : https://www.codechef.com/users/kodeutility
# GitHub            : https://www.github.com/kodeutility
# Portfolio website : https://kodeutility.github.io/
# Author            : Kiran BG
#Question link      : https://www.codechef.com/problems/PERFCONT

for _ in range(int(input())):
    n_problems, n_participants  = (map(int,input().split()))
    n_cakewalk = 0
    n_hard = 0
    n_solving_ith_problem = tuple(map(int,input().split()))

    for i in n_solving_ith_problem:
        if i>=(n_participants//2):
            n_cakewalk += 1
        elif i<=(n_participants//10):
            n_hard += 1

    if (n_cakewalk == 1) and (n_hard == 2):
        print("yes")
    else:
        print("no")
