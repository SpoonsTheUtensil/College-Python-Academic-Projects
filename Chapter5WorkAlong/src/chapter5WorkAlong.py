'''
Created on Sep 23, 2019

@author: 16368
'''

# Set variable SENTINEL
again = True

# Run the outer loop
while again:
    # Input special char and set height
    triangle_char = input("Enter a character: ")
    triangle_height = int(input("Enter triangle height: "))
    print()
    
    # Draw right triangle
    i = 0
    
    # Version 1
    while i < triangle_height:
        j = 0
        while j <= i:
            print(triangle_char, end=' ')
            j = j + 1
        print()
        i = i + 1
    
    # Version 2
    for count in range(triangle_height):
        print((triangle_char + " ") * (count+1))
        
    print()
    # Ask if user wants to retry
    YN = input("Would you like to run again? ")
    if YN == "no" or YN == "No":
        again = False