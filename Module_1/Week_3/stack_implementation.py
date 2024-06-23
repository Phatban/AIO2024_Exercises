'''
3. Thực hiện xây dựng class Stack với các phương thức (method) sau đây
    • initialization method nhận một input "capacity": dùng để khởi tạo stack với capacity là số
lượng element mà stack có thể chứa
    • .is_empty(): kiểm tra stack có đang rỗng
    • .is_full(): kiểm tra stack đã full chưa
    • .pop(): loại bỏ top element và trả về giá trị đó
    • .push(value) add thêm value vào trong stack
    • .top() lấy giá trị top element hiện tại của stack, nhưng không loại bỏ giá trị đó
'''


class MyStack:
    """
    Stack data structure implementation.
    """

    def __init__(self, capacity: int):
        """
        Initialize a Stack object.

        Args:
            capacity (int): Maximum capacity of the stack.
        """
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def is_full(self):
        """
        Check if the stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return len(self.stack) == self.capacity

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
            Any: The top element of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, value):
        """
        Add an element to the top of the stack.

        Args:
            value (Any): The value to be added to the stack.
        """
        if self.is_full():
            raise OverflowError("Stack is full")
        self.stack.append(value)

    def top(self):
        """
        Return the top element of the stack without removing it.

        Returns:
            Any: The top element of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.stack[-1]
