'''
1. Viết function thực hiện đánh giá classification model bằng F1-Score.
- Input: function nhận 3 giá trị tp, fp, fn
- Output: print ra kết quả của Precision, Recall, và F1-score
'''

def caculate_f1_score(tp, fp, fn):
    """
    Evaluates a classification model using F1-Score.

    Args:
        tp: Number of true positives. (must be a positive integer)
        fp: Number of false positives. (must be a positive integer)
        fn: Number of false negatives. (must be a positive integer)

    Returns:
        None. Prints the Precision, Recall, and F1-score.
    """

    # Check if input values are positive integers
    inputs = {'tp' : tp,
              'fp' : fp, 
              'fn' : fn }
    are_all_positive = True
    for key, value in inputs.items():
        if not isinstance(value, int):
            print(f'{key} must be int')
            return
        if value <= 0:
            are_all_positive = False
    if not are_all_positive:
        print('tp and fp and fn must be greater than zero')
        return

    # Caculate Precision, Recall, and F1-Score
    precision   = tp/(tp + fp)
    recall      = tp/(tp + fn)
    f1_score    = 2*(precision * recall)/(precision + recall)

    # Print results
    print('Precision is', precision)
    print('Recall is'   , recall)
    print('F1-Score is' , f1_score)
