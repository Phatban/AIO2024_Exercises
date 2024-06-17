'''
2. Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện
- Input: một từ.
- Output: dictionary đếm số lần các chữ xuất hiện.
'''


def character_count(word):
    """
    Count the occurrences of each character in a word.

    Args:
        word (str): A string representing the word.

    Returns:
        dict: A dictionary where the keys are characters and 
        the values are their corresponding counts.
    """
    dict_of_chars = {}
    for char in word:
        if char in dict_of_chars:
            dict_of_chars[char] += 1
        else:
            dict_of_chars[char] = 1
    return dict_of_chars
