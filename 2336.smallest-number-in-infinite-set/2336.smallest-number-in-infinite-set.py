from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.smallest_inf = 1
        self.h = []
        self.sms = set()

    def popSmallest(self) -> int:
        if len(self.h) > 0:
            self.sms.remove(self.h[0])
            return heappop(self.h)
        else:
            self.smallest_inf += 1
            return self.smallest_inf - 1

    def addBack(self, num: int) -> None:
        if num < self.smallest_inf:
            if num in self.sms:
                return
            self.sms.add(num)
            heappush(self.h, num)