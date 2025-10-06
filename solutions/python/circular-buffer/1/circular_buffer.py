class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def read(self):
        if not self.data:
            raise BufferEmptyException("Circular buffer is empty")
        return self.data.pop(0)

    def write(self, data):
        if len(self.data) < self.capacity:
            self.data.append(data)
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        data_len = len(self.data)
        if data_len < self.capacity:
            self.data.append(data)
        else:
            self.data.pop(0)
            self.data.append(data)

    def clear(self):
        self.data.clear()
