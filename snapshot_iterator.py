from typing import Dict, List, Iterator, Optional
# https://www.hack2hire.com/companies/databricks/coding-questions/68504e6d839fbdf76404b1d0/practice?questionId=68504f81839fbdf76404b1d1

class SnapshotSet:
    class _Node:
        def __init__(self, value, born):
            self.value = value
            self.born = born
            self.died = -1
            self.prev = None
            self.next = None

    def _append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def __init__(self):
        self.head = SnapshotSet._Node(None, -1)
        self.tail = SnapshotSet._Node(None, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.val_to_node = {}
        self.op_counter = 0

    def add(self, n: int) -> bool:
        if n in self.val_to_node:
            return False

        node = SnapshotSet._Node(n, self.op_counter)
        self.op_counter += 1
        self._append(node)
        self.val_to_node[n] = node
        return True

    def remove(self, n: int) -> bool:
        if n not in self.val_to_node:
            return False
        node = self.val_to_node[n]
        node.died = self.op_counter
        self.op_counter += 1
        del self.val_to_node[n]
        return True

    def contains(self, n: int) -> bool:

        return n in self.val_to_node

    def getIterator(self) -> Iterator[int]:
        counter = self.op_counter
        self.op_counter += 1
        return SnapshotSet.SnapshotIterator(
            self.head.next,
            self.tail,
            counter
        )

    class SnapshotIterator:
        def __init__(self, start: 'SnapshotSet._Node', tail: 'SnapshotSet._Node', counter: int):
            self.current = start
            self.tail = tail
            self.counter = counter

        def _skip_invalid(self):
            while self.current != self.tail:
                alive = (
                        self.current.born <= self.counter and self.current.died > self.counter
                )
                if alive:
                    break
                self.current = self.current.next

        def __iter__(self) -> 'SnapshotSet.SnapshotIterator':
            return self

        def __next__(self) -> int:
            if not self.hasNext():
                raise StopIteration
            val = self.current.value
            self.current = self.current.next
            self._skip_invalid()
            return val

        def hasNext(self) -> bool:
            return self.current != self.tail


# Helper function to iterate all elements in the iterator for easier visualization
def iterateAllElements(it: Iterator[int]) -> List[int]:
    return list(it)


def test1():
    print("======== test 1: =========")
    s = SnapshotSet()
    print(s.add(1))  # Expected: True
    print(s.add(2))  # Expected: True
    print(s.add(3))  # Expected: True
    print(s.add(4))  # Expected: True
    print(s.add(1))  # Expected: False
    it1 = s.getIterator()
    print(s.remove(1))  # Expected: True
    print(s.remove(3))  # Expected: True
    print(s.remove(5))  # Expected: False
    it2 = s.getIterator()

    print(iterateAllElements(it1))  # Expected: [1, 2, 3, 4]
    print(iterateAllElements(it2))  # Expected: [2, 4]


def test2():
    print("======== test 2: =========")
    s = SnapshotSet()
    it1 = s.getIterator()
    print(s.add(10))  # Expected: True
    it2 = s.getIterator()
    print(s.add(20))  # Expected: True
    it3 = s.getIterator()
    print(s.add(30))  # Expected: True
    it4 = s.getIterator()
    print(s.remove(30))  # Expected: True
    it5 = s.getIterator()
    print(s.remove(20))  # Expected: True
    it6 = s.getIterator()
    print(s.remove(10))  # Expected: True
    it7 = s.getIterator()

    print(iterateAllElements(it1))  # Expected: []
    print(iterateAllElements(it2))  # Expected: [10]
    print(iterateAllElements(it3))  # Expected: [10, 20]
    print(iterateAllElements(it4))  # Expected: [10, 20, 30]
    print(iterateAllElements(it5))  # Expected: [10, 20]
    print(iterateAllElements(it6))  # Expected: [10]
    print(iterateAllElements(it7))  # Expected: []


def test3():
    print("======== test 3: =========")
    s = SnapshotSet()
    print(s.remove(5))  # Expected: False
    print(s.add(5))  # Expected: True
    print(s.remove(5))  # Expected: True
    print(s.add(5))  # Expected: True
    print(iterateAllElements(s.getIterator()))  # Expected: [5]


def test4():
    print("======== test 4: =========")
    s = SnapshotSet()
    print(s.add(1))  # Expected: True
    print(s.add(2))  # Expected: True
    print(s.add(3))  # Expected: True
    print(s.add(4))  # Expected: True
    print(s.add(5))  # Expected: True
    it1 = s.getIterator()
    print(s.remove(2))  # Expected: True
    print(s.remove(4))  # Expected: True
    print(s.add(6))  # Expected: True
    it2 = s.getIterator()
    print(iterateAllElements(it1))  # Expected: [1, 2, 3, 4, 5]
    print(iterateAllElements(it2))  # Expected: [1, 3, 5, 6]


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()