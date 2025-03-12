original_array = [1, 2, 7, -2, -55, 1, 27, 42, -55]
new_array = [x + 2 for x in original_array if x > 5]
new_array_no_duplicates = list(set(new_array))
print(original_array)
print(new_array_no_duplicates)