def sort_strings_by_length(strings):
    return sorted(strings, key=len)


input_array = ["Toyota", "Honda", "Ford", "Chevrolet", "Mercedes Benz"]
sorted_array = sort_strings_by_length(input_array)
print(sorted_array)