list = [23, 45, 67, 8, 79]

for j in range(0, len(list) - 1):
    min_index = j
    for i in range(j + 1, len(list)):
        if list[i] < list[min_index]:
            min_index = i
    # Swap the found minimum element with the first element of the unsorted part
    list[j], list[min_index] = list[min_index], list[j]

print(list)
      
