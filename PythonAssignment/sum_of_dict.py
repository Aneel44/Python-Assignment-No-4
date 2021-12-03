# program to sum all the items in Dict.

def total_sum(mydict):

    total_sum = 0

    for i in mydict.values():
        total_sum = total_sum + i

    return total_sum

mydict = {0: 34, 1: 50, 2: 90, 3: 30}
print("sum of dict:", total_sum(mydict))
