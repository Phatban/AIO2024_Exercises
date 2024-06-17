'''
3. Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về 
một dictionary với key là từ và value là số lần từ đó xuất hiện.
- Input: Đường dẫn đến file txt
- Output: dictionary đếm số lần các từ xuất hiện
'''


def count_word(file_path):
    """
    Count the occurrences of each word in a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        dict: A dictionary where the keys are words and the values are their corresponding counts.
    """
    dict_of_words = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                if word in dict_of_words:
                    dict_of_words[word] += 1
                else:
                    dict_of_words[word] = 1
    return dict_of_words
