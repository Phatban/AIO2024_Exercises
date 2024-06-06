'''
4. Viết các functions để ước lượng 4 hàm số sin(x), cos(x), sinh(x), cosh(x).
- Input: x (số muốn tính toán) và n (số lần lặp muốn xấp xỉ)
- Output: Kết quả ước lượng hàm tương ứng với x.
'''

def factorial(n):
    """
    Calculate the factorial of a positive integer n.

    Args:
    n (int): The positive integer for which to calculate the factorial.

    Returns:
    int: The factorial of n.

    Raises:
    ValueError: If n is negative.
    """

    # Check input validity
    if n < 0:
        raise ValueError("Argument must be a positive integer.")

    # Base case: factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive call to calculate factorial of n - 1 and multiply by n
    return factorial(n - 1) * n

def approx_sin(x, n):
    """
    Approximate the value of sin(x) using the first n terms of the Taylor series.

    Args:
    x (float): The value of x.
    n (int): The number of terms of the Taylor series to use.

    Returns:
    float: The approximate value of sin(x).
    """
    result = 0
    for i in range(n):
        sign = (-1)**i  # Determine the sign of the term
        result += sign*(x**(2*i + 1))/factorial(2*i + 1) # Calculate the term value and add to the result
    return result

def approx_cos(x, n):
    """
    Approximate the value of cos(x) using the first n terms of the Taylor series.

    Args:
    x (float): The value of x.
    n (int): The number of terms of the Taylor series to use.

    Returns:
    float: The approximate value of cos(x).
    """
    result = 0
    for i in range(n):
        sign = (-1)**i  # Determine the sign of the term
        result += sign*(x**(2*i))/factorial(2*i) # Calculate the term value and add to the result
    return result

def approx_sinh(x, n):
    """
    Approximate the value of sinh(x) using the first n terms of the Taylor series.

    Args:
    x (float): The value of x.
    n (int): The number of terms of the Taylor series to use.

    Returns:
    float: The approximate value of sinh(x).
    """
    result = 0
    for i in range(n):
        result += (x**(2*i + 1))/factorial(2*i + 1) # Calculate the term value and add to the result
    return result

def approx_cosh(x, n):
    """
    Approximate the value of cosh(x) using the first n terms of the Taylor series.

    Args:
    x (float): The value of x.
    n (int): The number of terms of the Taylor series to use.

    Returns:
    float: The approximate value of cosh(x).
    """
    result = 0
    for i in range(n):
        result += (x**(2*i))/factorial(2*i) # Calculate the term value and add to the result
    return result
