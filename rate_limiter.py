import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls: int, period: float):
        self.max_calls = max_calls
        self.period = period
        self.timestamps = deque()

    def __call__(self):
        now = time.time()
        while self.timestamps and now - self.timestamps[0] > self.period:
            self.timestamps.popleft()

        if len(self.timestamps) >= self.max_calls:
            time_to_wait = self.period - (now - self.timestamps[0])
            time.sleep(time_to_wait)
            now = time.time()

        self.timestamps.append(now)
        return now

    def __enter__(self):
        self()
        return self

    def __exit__(self, *args):
        pass
