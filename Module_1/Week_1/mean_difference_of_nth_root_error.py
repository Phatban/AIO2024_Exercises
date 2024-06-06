'''
5. Viết function thực hiện Mean Difference of nth Root Error.
- Input: y (giá trị của y), y_hat (giá trị của y^), n (căn bậc n), và p (bậc của hàm loss).
- Output: Kết quả của hàm loss.
'''

def md_nre_single_sample(y, y_hat, n, p):
    """
    Compute the Mean Difference of nth Root Error (MD-nRE) for a single sample.

    Args:
        y (float): The true value of y.
        y_hat (float): The predicted value of y.
        n (int): The order of the root.
        p (int): The order of the loss function.

    Returns:
        float: The MD-nRE loss value.
    """
    # Calculate the nth root of y and y_hat
    y_root = y**(1/n)
    y_hat_root = y_hat**(1/n)

    # Calculate the difference between the nth roots
    difference = y_root - y_hat_root

    # Calculate the MD-nRE loss
    loss = difference**p

    # Print the loss value
    print(loss)
