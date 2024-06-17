'''
1. Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1.
- Input: num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] với k = 3.
- Output: [5, 5, 5, 5, 10, 12, 33, 33].
'''


def max_kernel(num_list, k):
    """
    Find the maximum element in a sliding window of size k in a list of integers.

    Args:
        num_list (list): A list of integers.
        k (int): The size of the sliding window.

    Returns:
        list: A list containing the maximum element in each sliding window of size k.
    """
    result = []
    queue = []

    for index, value in enumerate(num_list):
        # Remove elements from the queue that are outside the current window
        while queue and queue[0] <= index - k:
            queue.pop(0)

        # Remove elements smaller than value to maintain num_list[queue[0]] as the maximum
        while queue and num_list[queue[-1]] < value:
            queue.pop()

        queue.append(index)

        # When the window size is k, append the maximum element to the result
        if index >= k - 1:
            result.append(num_list[queue[0]])

    return result
