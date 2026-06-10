class TimeMap:

    def __init__(self):
        # Maps key -> list of [timestamp, value]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""
        
        # Binary search for the closest timestamp <= target timestamp
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # Potential candidate
                left = mid + 1        # Try to find a larger valid timestamp
            else:
                right = mid - 1       # Timestamp is too large, search left
                
        return res