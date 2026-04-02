class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.history = [{} for i in range(length)]
        self.snapshot = 0

    def set(self, index: int, val: int) -> None:
        self.history[index].update({self.snapshot: val})

    def snap(self) -> int:
        self.snapshot += 1
        return self.snapshot - 1

    def get(self, index: int, snap_id: int) -> int:
        for snapshot_id in reversed(sorted(self.history[index].keys())):
            if snapshot_id <= snap_id:
                return self.history[index][snapshot_id]
        return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)