def custom_sort(arr):
    n = len(arr)
    
    # Outer loop to traverse through all elements
    for i in range(n):
        # Inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Test cases with short and long lists
short_list = [5, 3, 8, 4, 2]
long_list = [12, 5, 7, 9, 1, 10, 15, 3, 6, 2]

# Sorting the lists
sorted_short_list = custom_sort(short_list.copy())
sorted_long_list = custom_sort(long_list.copy())

# Outputting the results
print("Original Short List: ", short_list)
print("Sorted Short List: ", sorted_short_list)

print("nOriginal Long List: ", long_list)
print("Sorted Long List: ", sorted_long_list)

# Estimating the number of comparisons
def estimate_comparisons(n):
    """
    Estimates the number of comparisons needed to sort a list of size n using Bubble Sort.
    
    :param n: Size of the list
    :return: Estimated number of comparisons
    """
    return (n * (n - 1)) // 2  # Total comparisons in Bubble Sort

# Estimating for lists of sizes 5 and 10
comparisons_5 = estimate_comparisons(5)
comparisons_10 = estimate_comparisons(10)
print(f"nEstimated comparisons for a list of 5 items: {comparisons_5}")
print(f"Estimated comparisons for a list of 10 items: {comparisons_10}")
