# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(arr):
    # Flatten the array using a for loop
    flattened_list = []
    for sublist in arr:
        flattened_list.extend(sublist)

    # Sort the flattened list
    flattened_and_sorted = sorted(flattened_list)
    return flattened_and_sorted

# Example usage
nested_array = [[3, 1, 4], [1, 5, 9], [2, 6, 5, 3, 5]]
result = flatten_and_sort(nested_array)
print(result)
