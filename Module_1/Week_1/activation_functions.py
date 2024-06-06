'''
2. Viết function mô phỏng theo 3 activation function.
- Input:
    + Người dùng nhập giá trị x.
    + Người dùng nhập tên activation function chỉ có 3 loại: sigmoid, relu, elu.
- Output: Kết quả f(x) khi x đi qua activation function tương ứng theo activation function name.
'''
import math
import numpy as np

def is_number(n):
    """
    Checks if the given input can be converted to a float.

    Args:
        n: The input to check.

    Returns:
        True if the input can be converted to a float, False otherwise.
    """
    try:
        float(n)    # Type - casting the string to "float"
                    # If string is not a valid "float", it'll raise "ValueError" exception
    except ValueError:
        return False
    return True

def caculate_activation_function():
    """
    Applies an activation function to a given value entered by the user.

    Args:
        None

    Returns:
        None

    Raises:
        ValueError: If the user-entered `x` is not a valid number.
        TypeError: If the user-entered activation function name is not valid.

    Prompts:
        - The user is prompted to enter x value.
        - The user is prompted to enter the activation function name (sigmoid|relu|elu).

    Prints:
        The caculated value of activation function.
    """
    # Prompt the user to enter the value of x
    x = input('Enter the value of x: ')

    # Check if x is a valid number
    if not is_number(x):
        print('x must be a number')
        return

    # Prompt the user to enter the activation function name
    function_name = input('Enter the activation function name (sigmoid, relu, or elu): ')

    # Apply the activation function
    x = float(x)
    e = math.e
    alpha = 0.01
    match function_name:
        case 'sigmoid':
            # Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
            f_x = 1 / (1 + e**(-x))
        case 'relu':
            # ReLU activation function: f(x) = max(0, x)
            f_x = max(0, x)
        case 'elu':
            # ELU activation function: f(x) = x if x >= 0, else alpha * (e^x - 1)
            f_x = np.where(x >= 0, x, alpha*(e**x - 1))
        case _:
            print(f'{function_name} is not supported.')
            return

    # Print the result
    print(f'{function_name}: f({x}) = {f_x}')
    return f_x
