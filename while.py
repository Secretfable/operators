my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    currient_number = my_list[i]
    i += 1
    if currient_number < 0:
        break
    elif currient_number > 0:
        print(currient_number)
    else:
        continue
