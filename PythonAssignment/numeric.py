#program to check if there any numeric value in list using for loop

lst = ["mango", "apple", 5 , "banana", 3.12]

for i in lst:
    if type(i) == int:
        print("Found numeric value in list", i)
    else:
        print("Not found")
