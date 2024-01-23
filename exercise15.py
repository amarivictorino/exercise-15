def exponent(base, exp):
    # Ensure that the exponent is non-negative
    if exp < 0:
        return "Exponent must be a non-negative integer."

    # Calculate the result using the ** operator
    result = base ** exp

    return result

# Example usage
base_1, exp_1 = 2, 5
result_1 = exponent(base_1, exp_1)
print(f"{base_1} raised to the power of {exp_1} is: {result_1}")

base_2, exp_2 = 5, 4
result_2 = exponent(base_2, exp_2)
print(f"{base_2} raised to the power of {exp_2} is: {result_2}")


