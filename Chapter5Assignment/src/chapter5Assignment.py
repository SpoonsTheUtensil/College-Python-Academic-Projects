'''
Created on Sep 23, 2019

@author: 16368
'''
# Set variables for arrow dimensions
arrow_base_height = int(input("Enter arrow base height:\n"))
arrow_base_width = int(input("Enter arrow base width:\n"))
arrow_head_width = int(input("Enter arrow head width:\n"))
print()

# While loop to check if the arrow head width is larger
# then the base
while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input("Enter arrow head width:\n"))
    print()

# For loop for creating the arrows base
for i in range(arrow_base_height):
    i = ('*' * arrow_base_width)
    print(i)

# For loop for creating the arrows head
for j in range(arrow_head_width):
    j = '*' * arrow_head_width
    print(j)
    arrow_head_width -= 1
    