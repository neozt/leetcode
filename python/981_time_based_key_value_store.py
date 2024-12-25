import bisect


class TimeMap:

    def __init__(self):
        self.map = {} # Map of key to sorted list


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''

        arr = self.map[key]

        print(arr)
        res = ""
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if timestamp < arr[middle][0]:
                right = middle - 1
            else:
                res = arr[middle][1]
                left = middle + 1

        return res


# Your TimeMap object will be instantiated and called as such:
timeMap = TimeMap();
timeMap.set("foo", "bar", 1)
# print(timeMap.get("foo", 1))
# print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
# print(timeMap.get("foo", 4))
# print(timeMap.get("foo", 5))
print(timeMap.get("foo", 1))

# ["TimeMap","set","get","get","set","get","get"]
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]