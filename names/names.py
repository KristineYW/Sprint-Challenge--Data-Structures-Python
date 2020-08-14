import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# STARTER CODE: ABOUT 6 SECONDS
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# USING A SET & FOR LOOP: UNDER 4 SECONDS
# Use a for-loop on each name in names_1. Use a set to avoid duplicates
# for x in set(names_1):
#     # Check to see if the name exists in names_2. Use a set to avoid duplicates
#     if x in set(names_2):
#         # If the name exists in both, add it to the duplicates list
#         duplicates.append(x)

# USING A FOR LOOP WITHOUT A SET: UNDER 2 SECONDS
# Use a for-loop on each name in names_1. Use a set to avoid duplicates
# for x in names_1:
#     # Check to see if the name exists in names_2. Use a set to avoid duplicates
#     if x in names_2:
#         # If the name exists in both, add it to the duplicates list
#         duplicates.append(x)

# USING A SET TO FIND THE INTERSECTION: UNDER 1 SECOND (about 0.004 seconds)
# names_as_set = set(names_1)
# intersection = names_as_set.intersection(names_2)

# duplicates = list(intersection)

# print(duplicates)

# USING A BST: ABOUT 0.12 SECONDS
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Check if the value is less than the current node's value 
        if value < self.value:
            # Does the current node have a left child?
            if self.left is None:
                self.left = BSTNode(value)
            # Otherwise, it doesn't have a left child and we can park the new node here
            else: 
                self.left.insert(value)
        # Otherwise, the value is greater than or equal to the current node's value
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        else:
            return False

node = BSTNode("None")
for name_1 in set(names_1):
    node.insert(name_1)

for name_2 in set(names_2):
    if node.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
