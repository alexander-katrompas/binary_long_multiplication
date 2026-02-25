
# this program will demonstrate how binary long multiplication works.
# It will take two binary numbers as input and will output their product in binary.
# It will use strings to represent the binary numbers and will perform the
# multiplication using the standard long multiplication algorithm.
# operations will be constrained to 8 bits, so the result will be
# truncated to 8 bits if it exceeds that.

def binary_add(X, Y):
    """
    This function adds two binary numbers represented
    as strings and returns the result as a string.
    :param X: a binary number represented as a string
    :param Y: a binary number represented as a string
    :exceptions: none, the function assumes that the inputs are valid binary strings
    :return: the sum of X and Y as a binary string (8 bits)
    """

    # Initialize the result and carry
    result = ""
    carry = 0

    # Pad the shorter number with zeros
    max_length = max(len(X), len(Y))
    X = X.zfill(max_length)
    Y = Y.zfill(max_length)

    # Loop through each bit from right to left
    for i in range(max_length - 1, -1, -1):
        bit_sum = int(X[i]) + int(Y[i]) + carry
        result_bit = bit_sum % 2  # The result bit is the remainder when divided by 2
        carry = bit_sum // 2  # The new carry is the quotient when divided by 2
        result = str(result_bit) + result  # Prepend the result bit to the result string

    # If there's a carry left after the last addition, prepend it to the result
    if carry:
        result = '1' + result

    # constrain to 8 bits
    return result[-8:]

def binary_multiply(A, B):
    """
    This function multiplies two binary numbers represented as strings
    and returns the product as a string.
    :param A: a binary number represented as a string
    :param B: a binary number represented as a string
    :exceptions: none, the function assumes that the inputs are valid binary strings
    :return: the product of A and B as a binary string (8 bits)
    """

    # Initialize the product to 0
    product = "00000000"

    # Reverse the second number to facilitate multiplication
    B_reversed = B[::-1]

    # Loop through each bit in the second number
    for i in range(len(B_reversed)):
        if B_reversed[i] == '1':
            # If the bit is 1, add A shifted left by i positions to the product
            shifted_A = A + '0' * i  # Shift A left by i positions
            product = binary_add(product, shifted_A)  # Add shifted A to the product

    return product[-8:]

# this will work in 8 bits
A = "00001101"  # 13 in decimal
B = "00001011"  # 11 in decimal
# Perform the multiplication
result = binary_multiply(A, B)
print(f"A: {A} (decimal {int(A, 2)})")
print(f"B: {B} (decimal {int(B, 2)})")
print(f"Product: {result} (decimal {int(result, 2)})")

# this will NOT work in 8 bits
A = "11001101" # 205 in decimal
B = "11101011" # 235 in decimal
# Perform the multiplication
result = binary_multiply(A, B)
print(f"A: {A} (decimal {int(A, 2)})")
print(f"B: {B} (decimal {int(B, 2)})")
print(f"Product: {result} (decimal {int(result, 2)})")
