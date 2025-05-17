# # filter list
def filter_list(l):
    # return a new list withthe string filtered out
    return [item for item in l if isinstance(item, int)]
print(filter_list([1, 2, 'a', 'b',5]))

# masking
def maskify(cc):
    return '#' *(len(cc) -4) + cc[-4:]

# mfano used"
print (maskify('45564636536'))
print (maskify('123'))

# zoezi
import math
def is_square(n):
    if n < 0: 
        return False
    return math.isqrt(n) ** 2 == n  

# 15th may 2025
def open_or_senior(data):
    result = ["Senior" if age >= 55 and handicap >= 7 else "Open" for age, handicap in data]
    print(result)
    return result

# Example usage
open_or_senior([(45, 2), (60, 8), (33, 5), (58, 6)])

# triangle test
def is_triangle(a, b, c):
    result = a + b > c and a + c > b and b + c > a
    
    if result:
        print(f"Yes! The sides {a}, {b}, and {c} form a valid triangle.")
    else:
        print(f"No! The sides {a}, {b}, and {c} do not form a valid triangle.")
    
    return result

# Example usage
is_triangle(3, 4, 5)  # Should print a confirmation in the terminal

# satoo
def high_and_low(numbers):
    #convert the input str into a list of integers
    num_list =list (map(int,numbers.split()))
    #find the highest and lowest num
    return f"{max(num_list)} {min(num_list)}"

# mfano used
print(high_and_low("8 3 -5 42 -1 0 9 4 7 4 -4 42 -9"))



# digits solutions
def dig_pow(n, p):
    # Convert number to a list of digits
    digits = [int(d) for d in str(n)]
    
    # Compute the sum of digits raised to consecutive powers
    total = sum(d ** (p + i) for i, d in enumerate(digits))
    
    # angalia kama total is divisible by n
    return total // n if total % n == 0 else -1

# Example usage
print(dig_pow(89, 1))  # Output: 1
print(dig_pow(92, 1))  # Output: -1
print(dig_pow(695, 2)) # Output: 2

   