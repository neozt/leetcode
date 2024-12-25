from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.bottom = []  # Max heap holding bottom half elements
        self.top = []  # Min heap holding top half elements

    def addNum(self, num: int) -> None:
        if len(self.bottom) == 0:
            heappush(self.bottom, -num)
            return
        median = self.findMedian()
        if num > median:
            heappush(self.top, num)
        else:
            heappush(self.bottom, -num)

        self.balance()

    def balance(self):
        if len(self.bottom) == len(self.top) + 2:
            removed_from_bottom = heappop(self.bottom)
            heappush(self.top, -removed_from_bottom)
        elif len(self.top) == len(self.bottom) + 2:
            removed_from_top = heappop(self.top)
            heappush(self.bottom, -removed_from_top)



    def findMedian(self) -> float:
        if len(self.bottom) == len(self.top):
            return (-self.bottom[0] + self.top[0]) / 2
        elif len(self.bottom) > len(self.top):
            return -self.bottom[0]
        else:
            return self.top[0]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())

# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]