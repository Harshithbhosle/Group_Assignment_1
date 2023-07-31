# Title: Near Miss Finder
# File: Group_assignment_1.py

# External files necessary to run the program: None

# External files created by the program: None

# Programmers:
# - Harshith Bhosle (Harshithbhosle@lewisu.edu)
# - Hema Bharath Kumar (hemabharathkumarna@lewisu.edu)

# Course: CPSC 60500-001 - Software Engineering

# Date completed and submitted: 07/30/2023

# Explanation:
# This program finds near misses for a given value of n and k. It calculates the closest integer Z that minimizes the absolute difference between the sum of x^n and y^n and Z^n. The program takes user inputs for 'n' and 'k'with constraints on their values and then iterates over all combinations of x and y to find the near misses.It prints the values of x, y, and Z that yield the smallest relative miss, along with the corresponding miss and relative size.

# Resources used:
# - Python documentation: https://docs.python.org/
# - Stack Overflow for algorithm insights: https://stackoverflow.com/

# Custom exception class for invalid n values
class InvalidNException(Exception):
    "Invalid value passed to n"
    pass

# Custom exception class for invalid k values
class InvalidKException(Exception):
    "Invalid value passed to k"
    pass

# Method to calculate the relative miss and the nearest integer Z
def calculate_relative_miss(x, y, n):
    # Calculate the sum of x^n and y^n
    xn_yn = x**n + y**n
    
    # Find the integer Z and Z+1 that are closest to (x^n + y^n)^(1/n)
    z_lower = int(xn_yn**(1/n))
    z_upper = z_lower + 1
    
    # Calculate the misses for the lower and upper Z values
    miss_lower = abs(xn_yn - z_lower**n)
    miss_upper = abs(z_upper**n - xn_yn)
    
    # Determine the closest Z and the relative size of the miss
    if miss_lower < miss_upper:
        closest_z = z_lower
        relative_size = miss_lower / xn_yn
    else:
        closest_z = z_upper
        relative_size = miss_upper / xn_yn
        
    return closest_z, min(miss_upper, miss_lower), relative_size

# Method to find near misses for given n and k values
def find_near_misses(n, k):
    # Initialize variables to track the smallest relative size and the corresponding misses and values
    smallest_relative_size = float('inf')
    smallest_miss = None
    best_x, best_y, best_z = None, None, None
    
    # Iterate over all possible x and y combinations in the range [10, k]
    for x in range(10, k+1):
        for y in range(10, k+1):
            # Calculate the relative miss and the nearest integer Z for each x, y pair
            z, miss, relative_size = calculate_relative_miss(x, y, n)
            
            # Update the smallest relative size and corresponding values if a smaller miss is found
            if relative_size < smallest_relative_size:
                smallest_relative_size = relative_size
                smallest_miss = miss
                best_x, best_y, best_z = x, y, z
				
    # Print the results
    print(f"X: {best_x}, Y: {best_y}, Z: {best_z}")
    print(f"Smallest Miss: {smallest_miss}")
    print(f"Smallest Relative Size: {smallest_relative_size:.2%}")

if __name__ == "__main__":
    try:
        # Get input for n value from the user and validate it
        n = int(input("Enter the value of n (2<n<12): "))
        if n <= 2 or n >= 12:
            raise InvalidNException
        else:
            # Get input for k value from the user and validate it
            k = int(input("Enter the value of k: "))
            if k <= 10:
                raise InvalidKException
            else:
                # Find and print near misses for the given n and k values
                find_near_misses(n, k)
    
    except InvalidNException:
        print("Value of n should be 2 < n < 12.")
    except InvalidKException:
        print("Value of k should be < 10.")

input()
