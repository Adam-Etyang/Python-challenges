"""
- Create a list of all common elements between two lists list_a = [1, 2, 3, 4, 5] and list_b = [3, 4, 5, 6, 7].
- Hint: You'll want to iterate through list_a and check if each element is in list_b.
"""

if __name__ == "__main__":
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]
    common_elements = [value for value in list_a if value in list_b]
    print(common_elements)


