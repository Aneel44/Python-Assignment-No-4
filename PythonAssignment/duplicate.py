# program to idenupltify duplicate values from list.

from collections import Counter

lst = [1,4,5,2,5,1,5,6,8,4,8]

dup = Counter(lst)
print(dup)

new_lst = list([item for item in dup if dup[item] > 1])

print(new_lst)
