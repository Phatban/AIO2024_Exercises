'''
4. Viết chương trình tính khoảng cách chỉnh sửa tối thiểu Levenshtein. Khoảng cách Levenshtein thể
hiện khoảng cách khác biệt giữa 2 chuỗi ký tự. Khoảng cách Levenshtein giữa chuỗi S và chuỗi T
là số bước ít nhất biến chuỗi S thành chuỗi T thông qua 3 phép biến đổi là:
• Xoá một ký tự
• Thêm một ký tự
• Thay thế ký tự này bằng ký tự khác
'''


def levenshtein_distance(token1, token2):
    """
    Calculate the Levenshtein distance between two strings.

    The Levenshtein distance is the minimum number of single-character edits 
    (insertions, deletions, or substitutions) required to change one string into the other.

    Args:
        token1 (str): The first string.
        token2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    m, n = len(token1), len(token2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calculate the Levenshtein distance using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]
