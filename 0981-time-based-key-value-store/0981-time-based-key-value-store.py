class TimeMap:

    def __init__(self):
        self.timestampObject = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestampObject[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.timestampObject:
            return res
        timestampObjectItems = self.timestampObject[key]
        l,r = 0, len(timestampObjectItems) - 1
        
        while l <= r:
            m = l + (r - l)//2            
            if timestampObjectItems[m][0] <= timestamp:
                res = timestampObjectItems[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)