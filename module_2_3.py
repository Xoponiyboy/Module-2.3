my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
b = len(my_list)
print(b)
while a < b:
       if my_list[a] < 0:
           break
       print(my_list[a])
       a += 1