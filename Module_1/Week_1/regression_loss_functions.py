'''
3. Viết function lựa chọn regression loss function để tính loss
- Input:
    + Người dùng nhập số lượng sample (num_samples) được tạo ra (chỉ nhận integer numbers)
    + Người dùng nhập loss name (MAE, MSE, RMSE).
- Output: Print ra loss name, sample, predict, target, loss.
    + loss name : là tên hàm loss mà người dùng chọn.
    + sample    : là thứ tự sample được tạo ra. 
    + predict   : là số mà model dự đoán (random một số trong range [0,10)).
    + target    : là số mà momg muốn mode dự đoán đúng (random một số trong range [0,10)).
    + loss      : là kết quả khi đưa predict và target vào hàm loss.
'''

import random
import math

def calculate_loss():
    """
    Calculate the specified loss function for a given number of samples.

    Args:
        None

    Returns:
        None

    Raises:
        ValueError: If the user-entered `num_samples` is not a valid integer number.

    Prompts:
        - The user is prompted to enter the number of samples.
        - The user is prompted to enter the loss function name (MAE, MSE, or RMSE).

    Prints:
        For each sample:
            Loss Name: The name of the loss function entered by the user.
            Sample: The sample number.
            Predict: The randomly generated predicted value.
            Target: The randomly generated target value.
            Loss: The calculated loss value for the sample.

    """
    # Prompt the user to enter the number of samples
    num_samples = input('Input number of samples (integer number) which are generated: ')

    # Check if the input is a valid integer number
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return
    num_samples = int(num_samples)

    # Prompt the user to enter the loss function name
    loss_function = input('Input loss name: ') # Assume the user always enters a valid loss name (MAE|MSE|RMSE)

    # Generate random pred and target for each sample and calculate loss for each sample
    sum_loss = 0
    for i in range(num_samples):
        y_pred = random.uniform(0, 10)
        y_targ = random.uniform(0, 10)
        if loss_function == 'MAE':
            loss_per_sample = abs(y_targ - y_pred)
        else:
            loss_per_sample = (y_targ - y_pred)**2
        print(f'loss name: {loss_function}, sample: {i}, pred: {y_pred}, target : {y_targ}, loss: {loss_per_sample}')
        sum_loss += loss_per_sample

    final_loss = 1/num_samples * sum_loss

    if loss_function == 'RMSE':
        final_loss = math.sqrt(final_loss)

    print(f'final {loss_function}: {final_loss}')
