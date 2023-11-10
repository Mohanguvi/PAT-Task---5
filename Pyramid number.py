# creating a pyramid nuber from 1 to 20

n = 20

# for loop used to interpret to increment the range in row 
# similiar column value will be in increment
for row in range(1, n+1): 
    for col in range(1, row+1):
        print(col, end=" ") # Dispaly the result
    print()