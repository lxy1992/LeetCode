import Empty
class ArrayQueues:

    DEFAULT_CAPACITY = 10 # moderate capacity for all new queues

    def __init__(self):
        self._data = [None] * ArrayQueues.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_Empty(self):
        return self._size == 0

    def first(self):
        if self.is_Empty():
            raise Empty('Queues is Empty')
        return self._data[self._front]

    def deQueues(self):
        if self.is_Empty():
            raise Empty('Queues is Empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):

        if self._size == len(self._data):
            self._resize(len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data # keep track of existing list
        self._data = [None] * cap   # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old) # use old size as modulus
        self._front = 0  # front has been realigned


if __name__ == '__main__':
    Q = ArrayQueues()
    Q.enqueue(1)
    Q.enqueue(2)
    print Q.deQueues()
    print Q.first()