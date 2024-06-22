'''
4. Thực hiện xây dựng class Queue với các chức năng (method) sau đây
    • initialization method nhận một input "capacity": dùng để khởi tạo queue với capacity là
số lượng element mà queue có thể chứa
    • .is_empty(): kiểm tra queue có đang rỗng
    • .is_full(): kiểm tra queue đã full chưa
    • .dequeue(): loại bỏ first element và trả về giá trị đó
    • .enqueue(value) add thêm value vào trong queue
    • .front() lấy giá trị first element hiện tại của queue, nhưng không loại bỏ giá trị đó
'''


class MyQueue:
    """
    Queue data structure implementation.
    """

    def __init__(self, capacity: int):
        """
        Initialize a Queue object.

        Args:
            capacity (int): Maximum capacity of the queue.
        """
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def is_full(self):
        """
        Check if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return len(self.queue) == self.capacity

    def dequeue(self):
        """
        Remove and return the front element from the queue.

        Returns:
            Any: The front element of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def enqueue(self, value):
        """
        Add an element to the end of the queue.

        Args:
            value (Any): The value to be added to the queue.
        """
        if self.is_full():
            raise OverflowError("Queue is full")
        self.queue.append(value)

    def front(self):
        """
        Return the front element of the queue without removing it.

        Returns:
            Any: The front element of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.queue[0]
