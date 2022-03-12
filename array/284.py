# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.peek_elem = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_elem is None:
            self.peek_elem = self.it.next()
        return self.peek_elem

    def next(self):
        """
        :rtype: int
        """
        if self.peek_elem is not None:
            ans = self.peek_elem
            self.peek_elem = None
            return ans
        return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_elem is not None:
            return True 
        return self.it.hasNext()