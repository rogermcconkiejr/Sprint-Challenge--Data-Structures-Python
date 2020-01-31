import time
### Run Time ###
# The current run time for this solution is polynomial O(n^c), meaning that everytime one element is added
# the list, the number of operations needed to be preformed increases exponentially.  This is because there is a 
# loop inside of another loop, meaning for instance that everytime n is increased in list one, list one will have
# to run an entirely new loop to get through list two.
# I am attempting to implement a Binary Search tree to shorten run time to O(n log n).


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

################ Binary Search Tree #####################
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
     # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
############### End Binary Tree ##########################
# Insert names_1 into binary tree
duplicates = []

tree = BinarySearchTree(names_1[5000]) # Initialize Binary Search Tree with middle element in list
for record in range(len(names_1)):
    tree.insert(names_1[record])       # Insert each record from list1 into tree. 
for record2 in names_2:                # For each record in list 2, run .contains to see if that name is also 
    if tree.contains(record2):         # present in list 1.  If it is, append it to duplicates list.
        duplicates.append(record2)

### OLD SEARCH CODE ###
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

### Stretch ####
# duplicates = []
# for a, b in zip(names_1, names_2):
#     if a == b:
#         duplicates.append(a)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
