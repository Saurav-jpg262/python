# Example using sets to perform set operations
fruits1 = {"banana", "apple", "cherry"}
fruits2 = {"banana", "orange", "kiwi"}

#add element
fruits1.add("pear")
fruits2.add("pear")

#remove element
fruits1.remove("cherry")

# Union of sets
all_fruits = fruits1.union(fruits2)
# Intersection of sets
common_fruits = fruits1.intersection(fruits2)
# Difference of sets
unique_to_fruits1 = fruits1.difference(fruits2)

# Printing the results
print("All fruits:", all_fruits)
print("Common fruits:", common_fruits)
print("Fruits unique to fruits1:", unique_to_fruits1)