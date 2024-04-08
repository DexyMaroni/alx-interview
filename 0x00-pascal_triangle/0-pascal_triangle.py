#!/usr/bin/python3
"""AN Interview Chanllenge on Pascal Traingle"""



def pascalTriangle(num):
    """ Accepts a number(i.e an integer) and calculate the pascal traingle based on the nth number of rows """
# Create a list to store all rows
    triangle = []
# Get a variable to store the number of rows.
    for rows_num in range(num):

        # Create a row to represent the rows
        row = [None for _ in range(rows_num+1)]

# Set the first and last values to 1
        row[0], row[-1] = 1, 1
# Find a way to apply the binomial formula
        for j in range(1, len(row) - 1):
            row[j] = triangle[rows_num - 1] [j - 1] + triangle[rows_num - 1] [j]

        triangle.append(row)
    return triangle
