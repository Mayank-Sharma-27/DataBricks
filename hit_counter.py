from collections import deque
class HitCounter:

    def __init__(self):
        self.total_hits = 0
        self.hits = deque()

    def hit(self, timestamp):
        self.total_hits += 1
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] = self.hits[-1][1] + 1
        else:
            self.hits.append([timestamp, 1])
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.total_hits -= self.hits[0][1]
            self.hits.popleft()

    def get_hits(self, timestamp):
        print(self.hits)
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.total_hits -= self.hits[0][1]
            self.hits.popleft()
        return self.total_hits

if __name__ == "__main__":

    # Test 1: Example from the problem
    print("Test 1: Example from problem")
    h = HitCounter()
    h.hit(1)
    h.hit(2)
    h.hit(3)
    print(h.get_hits(4))    # expected 3
    h.hit(300)
    print(h.get_hits(300))  # expected 4
    print(h.get_hits(301))  # expected 3

    # Test 2: Multiple hits at the same timestamp
    print("\nTest 2: Multiple hits at same timestamp")
    h = HitCounter()
    h.hit(1)
    h.hit(1)
    h.hit(1)
    print(h.get_hits(1))    # expected 3

    # Test 3: All hits expired
    print("\nTest 3: All hits expired")
    h = HitCounter()
    h.hit(1)
    h.hit(2)
    print(h.get_hits(302))  # expected 0

    # Test 4: Hits exactly on the boundary
    print("\nTest 4: Boundary hit at exactly 300s ago")
    h = HitCounter()
    h.hit(1)
    print(h.get_hits(301))  # expected 0 (1 is exactly 300s before 301, so excluded)
    print(h.get_hits(300))  # expected 1 (1 is within window of 300)